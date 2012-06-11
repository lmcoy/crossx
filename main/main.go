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

func QDep(input *qdepInput) {
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
		fmt.Printf("error: %s\n", e)
		return
	}

	file, err := os.Create(*input.fileout)
	if err != nil {
		fmt.Printf("error: %s\n", err)
		return
	}
	defer file.Close()
	sqrts := *input.sqrts
	N := *input.N
	if N < 1000 {
		fmt.Printf("error: too few monte carlo integration iterations: %d\n", N)
		return
	}
	for i := 0; i < 12; i++ {
		Q := 25.0 + float64(i)*25.0
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
}

func Cross(input *crossInput) {

}

func main() {
	args := os.Args
	if len(args) < 2 {
		fmt.Printf("Too few arguments\n")
		return
	}

	switch args[1] {
	case "qdep":
		input := &qdepInput{}
		flagset := flag.NewFlagSet("qdep", flag.ExitOnError)
		flagset.Usage = func() {
			fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
			fmt.Fprintf(os.Stderr, "%s [[OPTIONS]] inputfile\n\nOptions:\n", os.Args[0])
			flagset.PrintDefaults()
		}
		input.sqrts = flagset.Float64("sqrts", 14000.0, "center of mass energy in GeV. (default: LHC sqrt(s) = 14 TeV)")
		input.fileout = flagset.String("o", "depq.out", "output file")
		input.pdf = flagset.String("pdf", "cteq6l", "pdf which should be used.")
		input.pdfType = flagset.String("pdfType", "LHGrid", "pdf type: LHGrid or LHPdf")
		input.N = flagset.Int("N", 5000000, "number of monte carlo integration iterations")
		flagset.Parse(args[2:])
		switch {
		case flagset.NArg() == 0:
			fmt.Printf("error: no input file found\n")
			return
		case flagset.NArg() > 1:
			fmt.Printf("error: too many input files. Only one is supported.")
			return
		default:
			nargs := flagset.Args()
			in := nargs[0]
			input.filein = &in
		}
		fmt.Println("inputfile: ", *input.filein)
		fmt.Println("outfile:   ", *input.fileout)
		fmt.Println("sqrts:         ", *input.sqrts)
		fmt.Println("pdf:       ", *input.pdf)
		fmt.Println("pdfType:   ", *input.pdfType)
		fmt.Println("N:         ", *input.N)
		QDep(input)
	case "cross":
		input := &crossInput{}
		flagset := flag.NewFlagSet("cross", flag.ExitOnError)
		input.sqrts = flag.Float64("sqrts", 14000.0, "center of mass energy in GeV. (default: LHC sqrt(s) = 14 TeV)")
		input.Q = flag.Float64("Q", 300.0, "refactorization scale in GeV")
		input.fileout = flagset.String("o", "depq.out", "output file")
		input.pdf = flagset.String("pdf", "cteq6l", "pdf which should be used.")
		input.pdfType = flagset.String("pdfType", "LHGrid", "pdf type: LHGrid or LHPdf")
		flagset.Parse(args[2:])
		// TODO: Implement
	default:
		fmt.Println("'", args[1], "' is not a command")
	}
}

/*func main() {
	// init pdfs
	pdf.Init("test",pdf.LHGrid)
	pdf.InitPDF(1)
	// init random number generator
	rand.Seed(time.Now().Unix())

	//p := hep.NewParameter(mu, M1, M2, tan_beta, m_su, m_sd)
	p, e := hep.NewParameterFromLheFile("out/150.lhe")
	if e != nil {
		fmt.Printf( "error: %s\n", e )
		return
	}

	file, err := os.Create("crossQ2.dat")
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		return
	}
	defer file.Close()
	s := 14000.0 * 14000.0
	for i := 0; i < 12; i++ {
		Q := 25.0 + float64(i)*25.0
		I, error := hep.Sigma(s, Q, p)
		fmt.Fprintf(file, "%e\t%e\t%e\n", Q, I, error)
	}

	// write DSigma & DSigma2 to ds.dat
	//file, err := os.Create("ds.dat")
	//if err != nil {
	//	fmt.Printf("Error: %s\n", err)
	//	return
	//}
	//defer file.Close()
	//for i := 0; i < 100; i++ {
	//	t := -1.0 + float64(i)*2.0/100.0
	//	fmt.Fprintf(file, "%e\t%e\t%e\n", t, hep.DSigma(s, t, p), hep.DSigma2(s, t, p))
	//}

}*/
