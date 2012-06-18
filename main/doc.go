/*
main calculates the cross section for pp -> 𝜒2^0 𝜒1^+.
 
the modes of main are
	qdep	Calculates the cross section for various values of Q.
	cross	Calculates the cross section.
they are called by
	main qdep  [[OPTIONS]] input file
	main cross [[OPTIONS]] input files

Calculating cross sections for various values of Q.

The mode qdep calculates the cross section for pp -> 𝜒2^0 𝜒1^+ with values from Q = 25..300 GeV (step size 25 GeV).

Flags for qdep
	sqrts	center of mass energy in GeV. (default: LHC √s = 14 TeV)
	o	output file (default: depq.out)
	pdf	pdf which should be used. (default: cteq6ll)
	pdfType	pdf type: LHGrid or LHPdf (default: LHGrid)
	N	number of monte carlo integration iterations (default: 5000000)

Example
	main qdep -o file.dat -N 100000 input.lhe
	
Calculating the cross section.

The mode cross calculates the cross section for pp -> 𝜒2^0 𝜒1^+.

Flags for cross
	sqrts	center of mass energy in GeV. (default: LHC √s = 14 TeV)
	o	output file (default: depq.out)
	pdf	pdf which should be used. (default: cteq6ll)
	pdfType	pdf type: LHGrid or LHPdf (default: LHGrid)
	N	number of monte carlo integration iterations (default: 5000000)
	Q	factorization scale in GeV. (default: 0.0)
		If Q equals 0.0 Q will be set to the average of the two neutralino masses.

Example
	main cross -o file.dat input1.lhe input2.lhe input3.lhe
 */
package documentation
