package nccross

import (
	"fmt"
	"math"
	"math/rand"
	"physics/hep"
	"physics/hep/pdf"
	"testing"
	"time"
)

// precalculated data (prospino with LHC 14 TeV)
// 𝜒_2^0 𝜒_1^+ production in LO. 
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
	{"testdata/cmssm10.1.1.spec", 0.037400},
	{"testdata/cmssm10.1.2.spec", 0.024800},
	{"testdata/cmssm10.1.3.spec", 0.016900},
	{"testdata/cmssm10.1.4.spec", 0.011900},
	{"testdata/cmssm10.1.5.spec", 0.008490},
	{"testdata/cmssm10.2.1.spec", 0.037700},
	{"testdata/cmssm10.2.2.spec", 0.025000},
	{"testdata/cmssm10.2.3.spec", 0.017100},
	{"testdata/cmssm10.2.4.spec", 0.012000},
	{"testdata/cmssm10.2.5.spec", 0.008570},
	{"testdata/cmssm10.3.1.spec", 0.060400},
	{"testdata/cmssm10.3.2.spec", 0.031400},
	{"testdata/cmssm10.3.3.spec", 0.017600},
	{"testdata/cmssm10.3.4.spec", 0.010400},
	{"testdata/cmssm10.3.5.spec", 0.006420},
	{"testdata/cmssm10.4.1.spec", 0.210000},
	{"testdata/cmssm10.4.2.spec", 0.122000},
	{"testdata/cmssm10.4.3.spec", 0.075500},
	{"testdata/cmssm10.4.4.spec", 0.048700},
	{"testdata/cmssm10.4.5.spec", 0.032600},
	{"testdata/cmssm40.1.1.spec", 0.035700},
	{"testdata/cmssm40.1.2.spec", 0.023800},
	{"testdata/cmssm40.1.3.spec", 0.016300},
	{"testdata/cmssm40.1.4.spec", 0.011500},
	{"testdata/cmssm40.1.5.spec", 0.008220},
	{"testdata/cmssm40.2.1.spec", 0.060300},
	{"testdata/cmssm40.2.2.spec", 0.016900},
	{"testdata/cmssm40.2.3.spec", 0.025700},
	{"testdata/cmssm40.2.4.spec", 0.018000},
	{"testdata/cmssm40.2.5.spec", 0.012700},
	{"testdata/cmssm40.3.1.spec", 0.208000},
	{"testdata/cmssm40.3.2.spec", 0.158000},
	{"testdata/cmssm40.3.3.spec", 0.122000},
	{"testdata/cmssm40.3.4.spec", 0.095600},
	{"testdata/cmssm40.3.5.spec", 0.075800},
	{"testdata/mgmsb1.1.spec", 0.209000},
	{"testdata/mgmsb1.2.spec", 0.120000},
	{"testdata/mgmsb1.3.spec", 0.073800},
	{"testdata/mgmsb1.4.spec", 0.021900},
	{"testdata/mgmsb1.5.spec", 0.032100},
	{"testdata/mgmsb2.1.1.spec", 0.456000},
	{"testdata/mgmsb2.1.2.spec", 0.283000},
	{"testdata/mgmsb2.1.3.spec", 0.185000},
	{"testdata/mgmsb2.1.4.spec", 0.126000},
	{"testdata/mgmsb2.1.5.spec", 0.088100},
	{"testdata/mgmsb2.1.6.spec", 0.063500},
	{"testdata/mgmsb2.2.1.spec", 0.123000},
	{"testdata/mgmsb2.2.2.spec", 0.089100},
	{"testdata/mgmsb2.2.3.spec", 0.066600},
	{"testdata/mgmsb2.2.4.spec", 0.050700},
	{"testdata/mgmsb2.2.5.spec", 0.039200},
	{"testdata/mgmsb2.2.6.spec", 0.030700},
}

func TestSigma(t *testing.T) {
	pdf.Init("cteq6ll", pdf.LHGrid)
	fmt.Println("This test takes a long time... hang on!")
	// init random number generator
	rand.Seed(time.Now().Unix())

	onesigma := 0
	twosigma := 0
	threesigma := 0

	// perform tests
	for i, tt := range tests {
		t.Log("starting calculation of cross section")
		fmt.Printf("lhe file (%2d/%d): %5.1f %% done\n", i+1, len(tests), 100.0*float64(i)/float64(len(tests)))
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
		N := 100000
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
