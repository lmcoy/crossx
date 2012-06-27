/*
main calculates the cross section for pp → 𝜒^0 𝜒^+.

the modes of main are
	qdep      Calculates the cross section for various values of Q.
	cross     Calculates the cross section.
	dsigma    Calculates dsigma/dcos(theta).
they are called by
	main qdep  [[OPTIONS]] input file
	main cross [[OPTIONS]] input files
	main dsigma [[OPTIONS]] input file

Calculating cross sections for various values of Q.

The mode qdep calculates the cross section for pp → 𝜒^0 𝜒^+ with values from Q = qmin..qmax GeV.

Flags for qdep
	sqrts         center of mass energy in GeV. (default: LHC √s = 14 TeV)
	o             output file (default: depq.out)
	pdf           pdf which should be used. (default: cteq6ll)
	pdfType       pdf type: LHGrid or LHPdf (default: LHGrid)
	N             number of monte carlo integration iterations (default: 5000000)
	qmin          minimal value of Q in GeV (default: 100)
	qmax          maximal value of Q in GeV (default: 500)
	steps         number of different Q (default: 10)
	neutralino    selects neutralino (default: 2)
	chargino      selects chargino (default: 1)
	v             verbose output

Example
	main qdep -o file.dat -N 100000 input.lhe

Calculating the cross section.

The mode cross calculates the cross section for pp → 𝜒^0 𝜒^+.

Flags for cross
	sqrts         center of mass energy in GeV. (default: LHC √s = 14 TeV)
	o             output file (default: depq.out)
	pdf           pdf which should be used. (default: cteq6ll)
	pdfType       pdf type: LHGrid or LHPdf (default: LHGrid)
	N             number of monte carlo integration iterations (default: 5000000)
	Q             factorization scale in GeV. (default: 0.0)
	              If Q equals 0.0 Q will be set to the average of the two neutralino masses.
	neutralino    selects neutralino (default: 2)
	chargino      selects chargino (default: 1)
	v             verbose output

Calculates dsigma/dcos(theta)

The mode dsigma calculates the differential cross section for qq_ → 𝜒^0 𝜒^+

Flags for dsigma
	sqrts         center of mass energy in GeV. (default: LHC √s = 14 TeV)
	o             output file (default: dsigma.out)
	quarks        initial state quarks. Expected "ud", "cs" (default: "ud")
	samples       the sampling rate of dsigma/dcos(theta). (default: 30)
	neutralino    selects neutralino (default: 2)
	chargino      selects chargino (default: 1)
	v             verbose output

Example
	main cross -o file.dat input1.lhe input2.lhe input3.lhe
*/
package documentation
