package main

import (
	"fmt"
	"math/rand"
	"os"
	"physics/hep"
	"physics/hep/pdf"
	"time"
)

func main() {
	// init pdfs
	pdf.Init("test")
	pdf.InitPDF(1)
	// init random number generator
	rand.Seed(time.Now().Unix())

	/*M1 := 1.01396534E+02
	M2 := 1.91504241E+02
	tan_beta := 10.0
	m_sd := 1.55931152E+03
	m_su := 1.55431328E+03
	mu := 3.57680977E+02*/
	//p := hep.NewParameter(mu, M1, M2, tan_beta, m_su, m_sd)
	p, e := hep.NewParameterFromLheFile("out/450.lhe")
	if e != nil {
		fmt.Printf( "error: %s\n", e )
		return
	}
	s := 14000.0 * 14000.0
	I, error := hep.Sigma(s, p)

	fmt.Printf("m_chi_0 = %8.3f\tm_chi_+ = %8.3f\tsigma = %8.3f +- %8.3f pb\n", p.M_i, p.M_j, I, error)

	// write DSigma & DSigma2 to ds.dat
	file, err := os.Create("ds.dat")
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		return
	}
	defer file.Close()
	for i := 0; i < 100; i++ {
		t := -1.0 + float64(i)*2.0/100.0
		fmt.Fprintf(file, "%e\t%e\t%e\n", t, hep.DSigma(s, t, p), hep.DSigma2(s, t, p))
	}

}
