package nccross

import (
	"math"
	"math/rand"
	"physics/hep"
	"physics/hep/pdf"
	"testing"
	"time"
)

// precalculated data (prospino with LHC 14 TeV)
// chi_2^0 chi_1^+ production in LO. 
// Q = average of neutralino and chargino mass.
var tests = []struct {
	file   string
	crossx float64
}{
	{"testdata/120.lhe", 32.3},
	{"testdata/140.lhe", 13.2},
	{"testdata/150.lhe", 9.21},
	{"testdata/170.lhe", 4.92},
	{"testdata/190.lhe", 2.88},
	{"testdata/210.lhe", 1.81},
	{"testdata/225.lhe", 1.31},
	{"testdata/250.lhe", 0.816},
	{"testdata/275.lhe", 0.534},
	{"testdata/300.lhe", 0.364},
	{"testdata/325.lhe", 0.257},
	{"testdata/350.lhe", 0.186},
	{"testdata/375.lhe", 0.138},
	{"testdata/400.lhe", 0.104},
	{"testdata/450.lhe", 0.0628},
}

func TestSigma(t *testing.T) {
	pdf.Init("cteq6ll", pdf.LHGrid)

	// init random number generator
	rand.Seed(time.Now().Unix())

	onesigma := 0
	twosigma := 0
	threesigma := 0

	// perform tests
	for _, tt := range tests {
		t.Log("starting calculation of cross section")
		p, e := NewParameterFromLheFile(tt.file)
		t.Logf("    using %s as input file.\n", tt.file)
		if e != nil {
			t.Errorf("error: %s\n", e)
			continue
		}
		// set factorization scale to average of neutralino chargino mass
		M_i := p.M_n[1]
		M_j := p.M_c[0]
		Q := (M_i + M_j) / 2.0
		t.Logf("    using Q = %8.3f GeV as factorization scale.", Q)

		sqrts := 14.0 * hep.TeV
		t.Logf("    using √s = %8.3f GeV.", sqrts)
		N := 600000
		t.Logf("    using N = %d monte carlo iterations", N)
		I, error := Sigma(1, 0, sqrts*sqrts, Q, N, p)

		if math.Abs(I-tt.crossx) > 4.0*error {
			away := math.Abs(I-tt.crossx) / error
			t.Error("error: Calculated cross section not in 4 sigma interval of precalculated cross section.")
			t.Errorf("    calculated cross section: %8.3f +- %8.3f\n", I, error)
			t.Errorf("    expected cross section:   %8.3f\n", tt.crossx)
			t.Errorf("    %4.1f sigma away from precalculated result\n", away)
			continue
		} else {
			away := math.Abs(I-tt.crossx) / error
			t.Logf("    cross section = %8.3f +- %8.3f   (%4.1f sigma away from precalculated result)\n", I, error, away)
			switch {
			case away <= 1.0:
				onesigma += 1
				twosigma += 1
				threesigma += 1
			case away > 1.0 && away <= 2.0:
				twosigma += 1
				threesigma += 1
			case away > 2.0 && away <= 3.0:
				threesigma += 1
			default:
			}
		}
	}
	t.Log("\n--------------------------------------------------------------\n")
	t.Logf("%d cross sections calculated: (1 cross section -> %3.1f %%)\n", len(tests), 100.0/float64(len(tests)))
	t.Logf("    %4.2f %% in 1 sigma. (68.27 %% expected)\n", float64(onesigma)/float64(len(tests))*100.0)
	t.Logf("    %4.2f %% in 2 sigma. (95.45 %% expected)\n", float64(twosigma)/float64(len(tests))*100.0)
	t.Logf("    %4.2f %% in 3 sigma. (99.73 %% expected)\n", float64(threesigma)/float64(len(tests))*100.0)
	if t.Failed() {
		t.Log("\nThere were results which were not in the 4 sigma interval.",
			"This is possible. Maybe you should rerun the test to see whether this happens again!")
	}
}
