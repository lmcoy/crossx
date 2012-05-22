package main

import (
	//"physics/math"
	"fmt"
	"html/template"
	"io"
	"math"
	"net/http"
	"os"
	"physics/physics"
	"physics/physics/pdf"
	"physics/math/mcintegrator"
	"math/rand"
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
	/*A := math3d.NewMatrix4()
	A.SetRow( 0, &math3d.Vector4D{60.000,  0.000, -10.612, 42.449} )
	A.SetRow( 1,  &math3d.Vector4D{0.000, 120.000, 19.352, -77.408} )
	A.SetRow( 2, &math3d.Vector4D{-10.612, 19.352,  0.000, -277.000} )
	A.SetRow( 3, &math3d.Vector4D{42.449, -77.408, -277.000,  0.000} )

	Q, R := A.QRDecomposition()

	evalues, evectors := A.Eigen()

	B := Q.Times(R)

	C := A.Times(evectors)
	e,_ := evectors.Inverted()
	C = e.Times(C)

	fmt.Printf( "A = %s\n", A )
	fmt.Printf( "Q = %s\n", Q )
	fmt.Printf( "R = %s\n", R )
	fmt.Printf( "B = %s\n", B )

	fmt.Printf( "EV = %s\n", evalues )
	fmt.Printf( "E = %s\n", evectors )

	fmt.Printf( "C = %s\n", C )*/
	pdf.Init("test")
	pdf.InitPDF(1)
	/*xfx := pdf.Xfx( 0.2, 2.0, pdf.UQuark )
	fmt.Printf( "-------> % 8.3f\n", xfx )

	A := math3d.NewMatrix2()
	A.SetRow( 0, &math3d.Vector2D{ 100.0 , 80.0 } )
	A.SetRow( 1, &math3d.Vector2D{ 0.0 , 200.0 } )

	U,V := A.SingularValueDecomposition()
	fmt.Printf( "A = %s\n", A )
	fmt.Printf( "U = %s\n", U )
	fmt.Printf( "V = %s\n", V )

	fmt.Printf( "V.A.U^T = %s\n", U.Transposed().Times(A).Times(V) )*/
	rand.Seed(time.Now().Unix())
	It, terror := integrator.Integrate3( func(x,y,z float64) float64 { return x*x*y*y*z*z }, []float64{-2.0,3.0,-1.0}, []float64{2.0,4.0,-0.5}, 100000 )
	fmt.Printf( "It = %8.3f +- %8.3f\n", It, terror )
	It, terror = integrator.Integrate3( func(x,y,z float64) float64 { return math.Sin(y)*z*z }, []float64{-2.0,3.0,-1.0}, []float64{2.0,4.0,-0.5},100000)
	fmt.Printf( "It = %8.5f +- %8.5f\n", It, terror )
	
	/*Q := 2.0
	x := 0.001
	for i := 0; i < 100; i++  {
		fmt.Printf( "%4.3f\t%6.3f\t%6.3f\t%6.3f\t%6.3f\n", x, pdf.Xfx(x, Q, pdf.Gluon ), pdf.Xfx(x,Q,pdf.DQuark), pdf.Xfx( x, Q, pdf.UQuark ), pdf.Xfx( x, Q, pdf.SQuark ) );
		x += 0.009;
	}*/
	
	/*for i := 0; i < 20; i++ {
		m12 := float64(130 + i*10)*/
		m12 := 150.0
		p := physics.NewParameter(m12)
		if p == nil {
			panic("p nil")
		}
		s := 14000.0*14000.0
		I, error := physics.Sigma( s, p )

		fmt.Printf("m_chi_0 = %8.3f\tm_chi_+ = %8.3f\tsigma = %8.3f +- %8.3f pb\n", p.M_i, p.M_j,I, error)
	/*}*/
	/*file, err := os.Create("ds.dat")
	if err != nil {
		fmt.Printf( "Error: %s\n", err )
		return
	}
	defer file.Close()
	for i := 0; i < 30; i++ {
		t := -1.0 + float64(i)*2.0/30.0
		fmt.Fprintf( file, "%e\t%e\t%e\n", t, physics.DSigma( s, t, p ), physics.DSigma2( s, t, p) )
	}*/
	
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
