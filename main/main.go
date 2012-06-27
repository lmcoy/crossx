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

// set verbose with flag
var verbose bool

func printf(format string, args ...interface{}) {
	if verbose {
		fmt.Printf(format, args...)
	}
}

func println(args ...interface{}) {
	if verbose {
		fmt.Println(args...)
	}
}

type qdepInput struct {
	sqrts      *float64
	filein     *string
	fileout    *string
	pdf        *string
	pdfType    *string
	N          *int
	qmin       *float64
	qmax       *float64
	steps      *int
	neutralino *int
	chargino   *int
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
		fmt.Println("unexpected pdf type:", *input.pdfType, "using LHPdf instead.")
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

	neutralino := *input.neutralino
	chargino := *input.chargino

	if neutralino < 1 || neutralino > 4 {
		fmt.Fprintf(os.Stderr, "error: there are only 4 neutralinos. expected: 1..4\n")
		return
	}
	if chargino < 1 || chargino > 2 {
		fmt.Fprintf(os.Stderr, "error: there are only 2 charginos. expected: 1,2\n")
		return
	}

	fmt.Fprintf(file, "# pp →  𝜒_%d^0 𝜒_%d^+ with √s = %.1f GeV\n", neutralino, chargino, sqrts)
	fmt.Fprintln(file, "# Q\tI\terror (abs)")
	for i := 0; i < steps; i++ {
		Q := qmin + float64(i)*step
		printf("Calculating cross section for pp →  𝜒_%d^0 𝜒_%d^+ with √s = %.1f GeV\n", neutralino, chargino, sqrts)
		printf("    using Q = %.2f GeV as factorization scale\n", Q)
		printf("    using %d monte carlo iterations\n", N)
		I, error := nccross.Sigma(neutralino-1, chargino-1, sqrts*sqrts, Q, N, p)
		fmt.Fprintf(file, "%e\t%e\t%e\n", Q, I, error)
	}
}

type crossInput struct {
	infiles    []string
	fileout    *string
	sqrts      *float64
	Q          *float64
	pdf        *string
	pdfType    *string
	N          *int
	neutralino *int
	chargino   *int
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
		println("unexpected pdf type:", *input.pdfType, "using LHPdf instead.")
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

	neutralino := *input.neutralino
	chargino := *input.chargino

	if neutralino < 1 || neutralino > 4 {
		fmt.Fprintf(os.Stderr, "error: there are only 4 neutralinos. expected: 1..4\n")
		return
	}
	if chargino < 1 || chargino > 2 {
		fmt.Fprintf(os.Stderr, "error: there are only 2 charginos. expected: 1,2\n")
		return
	}

	fmt.Fprintf(file, "# pp →  𝜒_%d^0 𝜒_%d^+ with √s = %.1f GeV\n", neutralino, chargino, sqrts)
	fmt.Fprintf(file, "# m(chi_%d^0) m(chi_%d^+)        Q          I       abs. error\n", neutralino, chargino)
	for _, filename := range input.infiles {
		printf("Calculating cross section from %s...\n", filename)
		i := neutralino - 1
		j := chargino - 1
		p, e := nccross.NewParameterFromLheFile(filename)
		if e != nil {
			fmt.Fprintf(os.Stderr, "error: %s\n", e)
			return
		}
		Q := *input.Q
		if Q == 0.0 {
			Q = (math.Abs(p.M_n[i]) + math.Abs(p.M_c[j])) / 2.0
		}
		if Q < 0.0 {
			fmt.Fprintf(os.Stderr, "error: refactorization scale Q is < 0: Q = %f\n", Q)
			return
		}
		printf("    process: pp →  𝜒_%d^0 𝜒_%d^+ with √s = %.1f GeV\n", neutralino, chargino, sqrts)
		printf("    using Q = %.2f GeV as factorization scale\n", Q)
		printf("    using %d monte carlo iterations\n", N)
		I, error := nccross.Sigma(i, j, sqrts*sqrts, Q, N, p)
		fmt.Fprintf(file, "% 12.4e % 10.4e % 10.4e % 10.4e % 10.4e\n", p.M_n[i], p.M_c[j], Q, I, error)
	}

}

type dsigmaInput struct {
	lhefile    *string
	outfile    *string
	quarks     *string
	sqrts      *float64
	samples    *int
	neutralino *int
	chargino   *int
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

	neutralino := *input.neutralino
	chargino := *input.chargino

	if neutralino < 1 || neutralino > 4 {
		fmt.Fprintf(os.Stderr, "error: there are only 4 neutralinos. expected: 1..4\n")
		return
	}
	if chargino < 1 || chargino > 2 {
		fmt.Fprintf(os.Stderr, "error: there are only 2 charginos. expected: 1,2\n")
		return
	}

	// open input file
	p, e := nccross.NewParameterFromLheFile(*input.lhefile)
	if e != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", e)
		return
	}

	fmt.Fprintf(file, "# dsigma/dcos(theta) for √s = %.1f\n# initial state: %s\n", sqrts, *input.quarks)
	fmt.Fprintf(file, "#final state: 𝜒_%d^0 𝜒_%d^+\n", neutralino, chargino)
	fmt.Fprintln(file, "#\n# cos(theta)    dsigma/dcos(theta)")
	for i := 0; i < samples; i++ {
		cosTheta := -1.0 + float64(i)*2.0/float64(samples-1)
		dsigma := nccross.DSigma(neutralino-1, chargino-1, sqrts*sqrts, cosTheta, quarks, p, nil)
		fmt.Fprintf(file, "%12.5e    %12.5e\n", cosTheta, dsigma)
	}
}

func main() {
	args := os.Args

	printUsage := func() {
		fmt.Fprintln(os.Stderr, "%s calculates the cross section for pp -> 𝜒^0 𝜒^+.", args[0])
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
		input.neutralino = flagset.Int("neutralino", 2, "selects neutralino")
		input.chargino = flagset.Int("chargino", 1, "selects chargino.")
		flagset.BoolVar(&verbose, "v", false, "verbose output")
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
		println("inputfile: ", *input.filein)
		println("outfile:   ", *input.fileout)
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
		input.neutralino = flagset.Int("neutralino", 2, "selects neutralino")
		input.chargino = flagset.Int("chargino", 1, "selects chargino.")
		flagset.BoolVar(&verbose, "v", false, "verbose output")
		flagset.Parse(args[2:])
		if flagset.NArg() <= 0 {
			fmt.Fprintln(os.Stderr, "error: No input file.")
			return
		}
		input.infiles = append(input.infiles, flagset.Args()...)
		println("inputfiles: ", input.infiles)
		println("outfile:    ", *input.fileout)
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
		input.neutralino = flagset.Int("neutralino", 2, "selects neutralino")
		input.chargino = flagset.Int("chargino", 1, "selects chargino.")
		flagset.BoolVar(&verbose, "v", false, "verbose output")
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
		println("infile:  ", *input.lhefile)
		println("outfile: ", *input.outfile)
		dsigma(input)
	default:
		fmt.Fprintf(os.Stderr, "'%s' is not a command", args[1])
		printUsage()
	}
}
