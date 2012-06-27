package main

import (
	"flag"
	"fmt"
	"math"
	"math/rand"
	"os"
	"physics/hep/nccross"
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
	qmin    *float64
	qmax    *float64
	steps   *int
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

	p, e := nccross.NewParameterFromLheFile(*input.filein)
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
	qmin := *input.qmin
	qmax := *input.qmax
	if qmin >= qmax {
		fmt.Fprintf(os.Stderr, "error: qmin must be greater than qmax: qmin = %6.3f, qmax = %6.3f\n", qmin, qmax)
		return
	}
	steps := *input.steps
	if steps < 2 {
		fmt.Fprintf(os.Stderr, "error: too few steps: %d\n", steps)
		return
	}
	step := (qmax - qmin) / float64(steps-1)
	fmt.Fprintln(file, "# Q\tI\terror (abs)")
	for i := 0; i < steps; i++ {
		Q := qmin + float64(i)*step
		fmt.Printf("Calculating cross section with Q = %8.3f GeV...\n", Q)
		I, error := nccross.Sigma(1, 0, sqrts*sqrts, Q, N, p)
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
		i := 1
		j := 0
		p, e := nccross.NewParameterFromLheFile(filename)
		if e != nil {
			fmt.Fprintf(os.Stderr, "error: %s\n", e)
			return
		}
		Q := *input.Q
		if Q == 0.0 {
			Q = (math.Abs(p.M_n[i]) + math.Abs(p.M_c[j])) / 2.0
			fmt.Printf("    using %8.2f as factorization scale\n", Q)
		}
		fmt.Printf("    using %d monte carlo iterations\n", N)
		if Q < 0.0 {
			fmt.Fprintf(os.Stderr, "error: refactorization scale Q is < 0: Q = %f\n", Q)
			return
		}
		I, error := nccross.Sigma(1, 0, sqrts*sqrts, Q, N, p)
		fmt.Fprintf(file, "% 12.4e % 10.4e % 10.4e % 10.4e % 10.4e\n", p.M_n[i], p.M_c[j], Q, I, error)
	}

}

type dsigmaInput struct {
	lhefile *string
	outfile *string
	quarks  *string
	sqrts   *float64
	samples *int
}

func dsigma(input *dsigmaInput) {
	// create out file
	file, err := os.Create(*input.outfile)
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

	samples := *input.samples
	if samples < 5 {
		fmt.Fprintf(os.Stderr, "error: too few samples: %d\n", samples)
	}

	quarks := 0
	switch {
	case *input.quarks == "ud":
		quarks = 0
	case *input.quarks == "cs":
		quarks = 1
	default:
		fmt.Fprintf(os.Stderr, "error: unkown quarks in initial state: %s. Expected \"ud\", \"cs\"\n", *input.quarks)
		return
	}

	// open input file
	p, e := nccross.NewParameterFromLheFile(*input.lhefile)
	if e != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", e)
		return
	}

	fmt.Fprintf(file, "# dsigma/dcos(theta) for √s = %8.1f, %s as initial state\n", sqrts, *input.quarks)
	fmt.Fprintln(file, "#\n# cos(theta)    dsigma/dcos(theta)")
	for i := 0; i < samples; i++ {
		cosTheta := -1.0 + float64(i)*2.0/float64(samples-1)
		dsigma := nccross.DSigma(1, 0, sqrts*sqrts, cosTheta, quarks, p, nil)
		fmt.Fprintf(file, "%12.5e    %12.5e\n", cosTheta, dsigma)
	}
}

func main() {
	args := os.Args

	printUsage := func() {
		fmt.Fprintln(os.Stderr, "%s calculates the cross section for pp -> 𝜒2^0 𝜒1^+.", args[0])
		fmt.Fprintf(os.Stderr, "\nUsage: \n    %s COMMAND OPTIONS\n\ncommands:\n", args[0])
		fmt.Fprintln(os.Stderr, "    qdep    -- Calculates the cross section for various values of Q.")
		fmt.Fprintln(os.Stderr, "    cross   -- Calculates the cross section.")
		fmt.Fprintln(os.Stderr, "    dsigma  -- Calculates the differential cross section.")
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
		input.qmin = flagset.Float64("qmin", 100.0, "minimal value of Q")
		input.qmax = flagset.Float64("qmax", 500.0, "maximal value of Q")
		input.steps = flagset.Int("steps", 10, "number of different Q")
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
		input.sqrts = flagset.Float64("sqrts", 14000.0, "center of mass energy in GeV. (default: LHC sqrt(s) = 14 TeV).")
		input.Q = flagset.Float64("Q", 0.0, "refactorization scale in GeV. If Q equals 0.0 Q will be set to the average of the two neutralino masses")
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
	case "dsigma":
		input := &dsigmaInput{}
		flagset := flag.NewFlagSet("dsigma", flag.ExitOnError)
		flagset.Usage = func() {
			fmt.Fprintf(os.Stderr, "Usage of %s:\n", args[1])
			fmt.Fprintf(os.Stderr, "%s %s [[OPTIONS]] inputfile\n\nOptions:\n", os.Args[0], args[1])
			flagset.PrintDefaults()
		}
		input.outfile = flagset.String("o", "dsigma.out", "output file")
		input.sqrts = flagset.Float64("sqrts", 14000.0, "center of mass energy in GeV. (default: LHC sqrt(s) = 14 TeV).")
		input.quarks = flagset.String("quarks", "ud", "Initial state quarks. Expected \"ud\", \"cs\".")
		input.samples = flagset.Int("samples", 30, "The sampling rate of dsigma/dcos(theta).")
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
			input.lhefile = &in
		}
		fmt.Println("infile:  ", *input.lhefile)
		fmt.Println("outfile: ", *input.outfile)
		fmt.Println("sqrts:   ", *input.sqrts)
		fmt.Println("quarks:  ", *input.quarks)
		fmt.Println("samples: ", *input.samples)
		dsigma(input)
	default:
		fmt.Fprintf(os.Stderr, "'%s' is not a command", args[1])
		printUsage()
	}
}
