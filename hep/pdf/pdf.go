// Package pdf provides parton distribution functions.
//
// This package is a simple go binding to http://lhapdf.hepforge.org/
package pdf

// #cgo LDFLAGS: -lpdf -lstdc++ -L/usr/local/lib -lLHAPDF
// #include "pdf.h"
import "C"

// Type represents a parton type.
type Type int

const (
	// Partons
	// Antiparticles
	TBarQuark Type = iota - 6
	BBarQuark
	CBarQuark
	SBarQuark
	UBarQuark
	DBarQuark
	// Gauge
	Gluon
	// Particles
	DQuark
	UQuark
	SQuark
	CQuark
	BQuark
	TQuark
	Photon
)

type PdfType int
const (
	LHGrid PdfType = 0
	LHPdf PdfType = 1
)

// Init initalizes the PDFs.
func Init(name string, typ PdfType) {
	C.InitPDFSet(C.CString(name), C.int(typ))
}

// Xfx returns x*f(x,Q) for the parton typ where f is the pdf and Q the factorization scale.
func Xfx(x, Q float64, typ Type) float64 {
	return float64(C.PDF_xfx(C.double(x), C.double(Q), C.int(typ)))
}
