package main

import (
	//"physics/math"
	"fmt"
	"html/template"
	"io"
	"math/rand"
	"net/http"
	"os"
	"physics/physics"
	"physics/physics/pdf"
	"time"
)

type Hello struct {
	Title         string
	SUSYParameter *physics.SUSY
}

func (h *Hello) ErrorPage(w io.Writer, code int, reason error) {
	fmt.Fprintf(w, "<html><head><title>Error %d</title></head><body><h1>Error %d: %s</h1></body></html>", code, code, reason)
}

func (h *Hello) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	switch r.URL.String() {
	case "/":
		test, ok := template.ParseFiles("test.templ")
		if ok != nil {
			h.ErrorPage(w, 1, ok)
		} else {
			ok = test.Execute(w, h)
		}
	default:
		file, err := os.Open("." + r.URL.String())
		if err != nil {
			h.ErrorPage(w, 404, err)
		} else {
			io.Copy(w, file)
			file.Close()
		}
	}
}

func main() {
	// init pdfs
	pdf.Init("test")
	pdf.InitPDF(1)
	// init random number generator
	rand.Seed(time.Now().Unix())

	M1 := 1.01396534E+02
	M2 := 1.91504241E+02
	tan_beta := 10.0
	m_sd := 5.68441109E+02
	m_su := 5.61119014E+02
	mu := 3.57680977E+02
	p := physics.NewParameter(mu, M1, M2, tan_beta, m_su, m_sd)
	if p == nil {
		panic("p nil")
	}
	s := 14000.0 * 14000.0
	I, error := physics.Sigma(s, p)

	fmt.Printf("m_chi_0 = %8.3f\tm_chi_+ = %8.3f\tsigma = %8.3f +- %8.3f pb\n", p.M_i, p.M_j, I, error)

	// write DSigma & DSigma2 to ds.dat
	file, err := os.Create("ds.dat")
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		return
	}
	defer file.Close()
	for i := 0; i < 30; i++ {
		t := -1.0 + float64(i)*2.0/30.0
		fmt.Fprintf(file, "%e\t%e\t%e\n", t, physics.DSigma(s, t, p), physics.DSigma2(s, t, p))
	}

	/*tmin := physics.Mandelstam_t( math.Pi, s, p.M_i, p.M_j )
	tmax := physics.Mandelstam_t( 0.0, s, p.M_i,p.M_j )
	step := (tmax-tmin)/1000.0
	fmt.Printf( "step: %e\n", step )
	for i := 0; i < 1000; i++ {
		t := tmin+float64(i)*step
		fmt.Printf( "%e\t%e\n", t, physics.DSigma(s, t, p) )
	}*/

	/*var h Hello
	h.SUSYParameter = &physics.SUSY{}
	http.ListenAndServe( "localhost:4000",&h )*/
}
