package main

import (
	"flag"
	"fmt"
	"math/rand"
	"os"
	"physics/hep"
	"physics/hep/pdf"
	"time"
)

type qdepInput struct {
	sqrts   *float64
	filein  *string
	fileout *string
	pdf     *string
	pdfType *string
	N       *int
}

func qdep(input *qdepInput) {
	// init pdfs
	var ptype pdf.PdfType
	switch *input.pdfType {
	case "LHPdf":
		ptype = pdf.LHPdf
	case "LHGrid":
		ptype = pdf.LHGrid
	default:
		fmt.Println("unexpected pdf type: ", *input.pdfType, " using LHPdf instead.")
		ptype = pdf.LHPdf
	}

	pdf.Init(*input.pdf, ptype)

	// init random number generator
	rand.Seed(time.Now().Unix())

	p, e := hep.NewParameterFromLheFile(*input.filein)
	if e != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", e)
		return
	}

	file, err := os.Create(*input.fileout)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", err)
		return
	}
	defer file.Close()

	// check input parameters
	sqrts := *input.sqrts
	if sqrts <= 0.0 {
		fmt.Fprintf(os.Stderr, "error: √s < 0: √s = %f\n", sqrts)
		return
	}
	N := *input.N
	if N < 1000 {
		fmt.Fprintf(os.Stderr, "error: too few monte carlo integration iterations: %d\n", N)
		return
	}
	fmt.Fprintln(file, "# Q\tI\terror (abs)")
	for i := 0; i < 12; i++ {
		Q := 25.0 + float64(i)*25.0
		fmt.Printf("Calculating cross section with Q = %8.3f GeV...\n", Q)
		I, error := hep.Sigma(sqrts*sqrts, Q, N, p)
		fmt.Fprintf(file, "%e\t%e\t%e\n", Q, I, error)
	}
}

type crossInput struct {
	infiles []string
	fileout *string
	sqrts   *float64
	Q       *float64
	pdf     *string
	pdfType *string
	N       *int
}

func cross(input *crossInput) {
	// init pdfs
	var ptype pdf.PdfType
	switch *input.pdfType {
	case "LHPdf":
		ptype = pdf.LHPdf
	case "LHGrid":
		ptype = pdf.LHGrid
	default:
		fmt.Println("unexpected pdf type: ", *input.pdfType, " using LHPdf instead.")
		ptype = pdf.LHPdf
	}

	pdf.Init(*input.pdf, ptype)

	// init random number generator
	rand.Seed(time.Now().Unix())

	// create out file
	file, err := os.Create(*input.fileout)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", err)
		return
	}
	defer file.Close()

	// check input parameters
	sqrts := *input.sqrts
	if sqrts <= 0.0 {
		fmt.Fprintf(os.Stderr, "error: √s < 0: √s = %f\n", sqrts)
		return
	}
	N := *input.N
	if N < 1000 {
		fmt.Fprintf(os.Stderr, "error: too few monte carlo integration iterations: %d\n", N)
		return
	}

	fmt.Fprintln(file, "# m(chi_2^0) m(chi_1^+)        Q          I       abs. error")
	for _, filename := range input.infiles {
		fmt.Printf("Calculating cross section from %s...\n", filename)
		p, e := hep.NewParameterFromLheFile(filename)
		if e != nil {
			fmt.Fprintf(os.Stderr, "error: %s\n", e)
			return
		}
		Q := *input.Q
		if Q == 0.0 {
			Q = (p.M_i + p.M_j) / 2.0
			fmt.Printf("    using %8.2f as factorization scale\n", Q)
		}
		fmt.Printf("    using %d monte carlo iterations\n", N)
		if Q < 0.0 {
			fmt.Fprintf(os.Stderr, "error: refactorization scale Q is < 0: Q = %f\n", Q)
			return
		}
		I, error := hep.Sigma(sqrts*sqrts, Q, N, p)
		fmt.Fprintf(file, "% 12.4e % 10.4e % 10.4e % 10.4e % 10.4e\n", p.M_i, p.M_j, Q, I, error)
	}

}

func main() {
	args := os.Args

	printUsage := func() {
		fmt.Fprintln(os.Stderr, "%s calculates the cross section for pp -> 𝜒2^0 𝜒1^+.", args[0])
		fmt.Fprintf(os.Stderr, "\nUsage: \n    %s COMMAND OPTIONS\n\ncommands:\n", args[0])
		fmt.Fprintln(os.Stderr, "    qdep    -- Calculates the cross section for various values of Q.")
		fmt.Fprintln(os.Stderr, "    cross   -- Calculates the cross section.")
		fmt.Fprintf(os.Stderr, "    For more information about the commands use \"%s command --help\".\n", args[0])
	}
	if len(args) < 2 {
		fmt.Fprintf(os.Stderr, "Too few arguments\n")
		printUsage()
		return
	}

	switch args[1] {
	case "qdep":
		input := &qdepInput{}
		flagset := flag.NewFlagSet("qdep", flag.ExitOnError)
		flagset.Usage = func() {
			fmt.Fprintf(os.Stderr, "Usage of %s:\n", args[1])
			fmt.Fprintf(os.Stderr, "%s %s [[OPTIONS]] inputfile\n\nOptions:\n", os.Args[0], args[1])
			flagset.PrintDefaults()
		}
		input.sqrts = flagset.Float64("sqrts", 14000.0, "center of mass energy in GeV. (default: LHC √s = 14 TeV)")
		input.fileout = flagset.String("o", "depq.out", "output file")
		input.pdf = flagset.String("pdf", "cteq6ll", "pdf which should be used.")
		input.pdfType = flagset.String("pdfType", "LHGrid", "pdf type: LHGrid or LHPdf")
		input.N = flagset.Int("N", 5000000, "number of monte carlo integration iterations")
		flagset.Parse(args[2:])
		switch {
		case flagset.NArg() == 0:
			fmt.Fprintln(os.Stderr, "error: no input file found")
			return
		case flagset.NArg() > 1:
			fmt.Fprintln(os.Stderr, "error: too many input files. Only one is supported.")
			return
		default:
			nargs := flagset.Args()
			in := nargs[0]
			input.filein = &in
		}
		fmt.Println("inputfile: ", *input.filein)
		fmt.Println("outfile:   ", *input.fileout)
		fmt.Println("sqrts:     ", *input.sqrts)
		fmt.Println("pdf:       ", *input.pdf)
		fmt.Println("pdfType:   ", *input.pdfType)
		fmt.Println("N:         ", *input.N)
		qdep(input)
	case "cross":
		input := &crossInput{infiles: make([]string, 0, 10)}
		flagset := flag.NewFlagSet("cross", flag.ExitOnError)
		flagset.Usage = func() {
			fmt.Fprintf(os.Stderr, "Usage of %s:\n", args[1])
			fmt.Fprintf(os.Stderr, "%s %s [[OPTIONS]] inputfiles\n\nOptions:\n", os.Args[0], args[1])
			flagset.PrintDefaults()
		}
		input.sqrts = flag.Float64("sqrts", 14000.0, "center of mass energy in GeV. (default: LHC sqrt(s) = 14 TeV).")
		input.Q = flag.Float64("Q", 0.0, "refactorization scale in GeV. If Q equals 0.0 Q will be set to the average of the two neutralino masses")
		input.fileout = flagset.String("o", "cross.out", "output file")
		input.pdf = flagset.String("pdf", "cteq6ll", "pdf which should be used.")
		input.pdfType = flagset.String("pdfType", "LHGrid", "pdf type: LHGrid or LHPdf.")
		input.N = flagset.Int("N", 5000000, "number of monte carlo integration iterations.")
		flagset.Parse(args[2:])
		if flagset.NArg() <= 0 {
			fmt.Fprintln(os.Stderr, "error: No input file.")
			return
		}
		input.infiles = append(input.infiles, flagset.Args()...)
		fmt.Println("inputfiles: ", input.infiles)
		fmt.Println("outfile:    ", *input.fileout)
		fmt.Println("sqrts:      ", *input.sqrts)
		fmt.Println("Q:          ", *input.Q)
		fmt.Println("pdf:        ", *input.pdf)
		fmt.Println("pdfType:    ", *input.pdfType)
		fmt.Println("N:          ", *input.N)
		cross(input)
	default:
		fmt.Fprintf(os.Stderr, "'%s' is not a command", args[1])
		printUsage()
	}
}
