#include "LHAPDF/LHAPDF.h"

#include "pdf.h"

void InitPDFSet( char * name, int typ ) {
	if (typ==0) {
		LHAPDF::initPDFSet( name, LHAPDF::LHPDF, 0 );
	} else {
		LHAPDF::initPDFSet( name, LHAPDF::LHGRID, 0 );
	}
}

void InitPDF( int i ) {
	LHAPDF::initPDF(i);
}

double PDF_xfx( double x, double Q, int type ) {
	return LHAPDF::xfx( x, Q, type );
}