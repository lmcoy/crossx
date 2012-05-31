package pdf

// #cgo LDFLAGS: -lpdf -lstdc++ -L/usr/local/lib -lLHAPDF
// #include "pdf.h"
import "C"

type Type int

const (
	TBarQuark Type = iota - 6
	BBarQuark
	CBarQuark
	SBarQuark
	UBarQuark
	DBarQuark
	Gluon
	DQuark
	UQuark
	SQuark
	CQuark
	BQuark
	TQuark
	Photon
)

// Init initalizes the PDFs.
func Init(name string) {
	C.InitPDFSet(C.CString("cteq6mE"))
}

func InitPDF(i int) {
	C.InitPDF(C.int(i))
}

// Xfx returns x*f(x,Q) for the parton typ where f is the pdf and Q the factorization scale.
func Xfx(x, Q float64, typ Type) float64 {
	return float64(C.PDF_xfx(C.double(x), C.double(Q), C.int(typ)))
}
