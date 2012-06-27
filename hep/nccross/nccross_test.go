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

type precalc struct {
	file   string
	crossx float64
}

// precalculated data (prospino with LHC 14 TeV)
// 𝜒_2^0 𝜒_1^+ production in LO. 
// Q = average of neutralino and chargino mass.
var tests = []precalc{
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

// precalculated data (prospino with LHC 14 TeV)
// 𝜒_3^0 𝜒_1^+ production in LO. 
// Q = average of neutralino and chargino mass.
// 𝜒_3^0 has negative mass!
var tests_20 = []precalc{
	{"testdata/120.lhe", 0.359000},
	{"testdata/140.lhe", 0.195000},
	{"testdata/150.lhe", 0.147000},
	{"testdata/170.lhe", 0.086000},
	{"testdata/190.lhe", 0.052800},
	{"testdata/210.lhe", 0.033700},
	{"testdata/225.lhe", 0.024600},
	{"testdata/250.lhe", 0.015000},
	{"testdata/275.lhe", 0.009570},
	{"testdata/300.lhe", 0.006280},
	{"testdata/325.lhe", 0.004240},
	{"testdata/350.lhe", 0.002930},
	{"testdata/375.lhe", 0.002070},
	{"testdata/400.lhe", 0.001490},
	{"testdata/450.lhe", 0.000806},
	{"testdata/cmssm10.1.1.spec", 0.000405},
	{"testdata/cmssm10.1.2.spec", 0.000249},
	{"testdata/cmssm10.1.3.spec", 0.000158},
	{"testdata/cmssm10.1.4.spec", 0.000103},
	{"testdata/cmssm10.1.5.spec", 0.000069},
	{"testdata/cmssm10.2.1.spec", 0.000406},
	{"testdata/cmssm10.2.2.spec", 0.000249},
	{"testdata/cmssm10.2.3.spec", 0.000158},
	{"testdata/cmssm10.2.4.spec", 0.000103},
	{"testdata/cmssm10.2.5.spec", 0.000069},
	{"testdata/cmssm10.3.1.spec", 0.000689},
	{"testdata/cmssm10.3.2.spec", 0.000318},
	{"testdata/cmssm10.3.3.spec", 0.000160},
	{"testdata/cmssm10.3.4.spec", 0.000085},
	{"testdata/cmssm10.3.5.spec", 0.000048},
	{"testdata/cmssm10.4.1.spec", 0.002190},
	{"testdata/cmssm10.4.2.spec", 0.001200},
	{"testdata/cmssm10.4.3.spec", 0.000702},
	{"testdata/cmssm10.4.4.spec", 0.000432},
	{"testdata/cmssm10.4.5.spec", 0.000276},
	{"testdata/cmssm40.1.1.spec", 0.000179},
	{"testdata/cmssm40.1.2.spec", 0.000116},
	{"testdata/cmssm40.1.3.spec", 0.000077},
	{"testdata/cmssm40.1.4.spec", 0.000053},
	{"testdata/cmssm40.1.5.spec", 0.000037},
	{"testdata/cmssm40.2.1.spec", 0.000295},
	{"testdata/cmssm40.2.2.spec", 0.000079},
	{"testdata/cmssm40.2.3.spec", 0.000122},
	{"testdata/cmssm40.2.4.spec", 0.000084},
	{"testdata/cmssm40.2.5.spec", 0.000058},
	{"testdata/cmssm40.3.1.spec", 0.000963},
	{"testdata/cmssm40.3.2.spec", 0.000756},
	{"testdata/cmssm40.3.3.spec", 0.000601},
	{"testdata/cmssm40.3.4.spec", 0.000483},
	{"testdata/cmssm40.3.5.spec", 0.000391},
	{"testdata/mgmsb1.1.spec", 0.061400},
	{"testdata/mgmsb1.2.spec", 0.040000},
	{"testdata/mgmsb1.3.spec", 0.027500},
	{"testdata/mgmsb1.4.spec", 0.012600},
	{"testdata/mgmsb1.5.spec", 0.014700},
	{"testdata/mgmsb2.1.1.spec", 0.028300},
	{"testdata/mgmsb2.1.2.spec", 0.017900},
	{"testdata/mgmsb2.1.3.spec", 0.011900},
	{"testdata/mgmsb2.1.4.spec", 0.008270},
	{"testdata/mgmsb2.1.5.spec", 0.005920},
	{"testdata/mgmsb2.1.6.spec", 0.004350},
	{"testdata/mgmsb2.2.1.spec", 0.000327},
	{"testdata/mgmsb2.2.2.spec", 0.000182},
	{"testdata/mgmsb2.2.3.spec", 0.000122},
	{"testdata/mgmsb2.2.4.spec", 0.000083},
	{"testdata/mgmsb2.2.5.spec", 0.000058},
	{"testdata/mgmsb2.2.6.spec", 0.000041},
}

func init() {
	// init pdfs
	pdf.Init("cteq6ll", pdf.LHGrid)
	// init random number generator
	rand.Seed(time.Now().Unix())
}

func testprecalc(neut, charg int, t *testing.T, p []precalc) {
	onesigma := 0
	twosigma := 0
	threesigma := 0

	lenp := len(p)
	// perform tests
	for i, tt := range p {
		t.Log("starting calculation of cross section")
		fmt.Printf("lhe file (%2d/%d): %5.1f %% done\r", i+1, lenp, 100.0*float64(i)/float64(lenp))
		p, e := NewParameterFromLheFile(tt.file)
		t.Logf("    using %s as input file.\n", tt.file)
		if e != nil {
			t.Errorf("error: %s\n", e)
			continue
		}
		// set factorization scale to average of neutralino chargino mass
		M_i := math.Abs(p.M_n[neut])
		M_j := math.Abs(p.M_c[charg])
		Q := (M_i + M_j) / 2.0
		t.Logf("    using Q = %8.3f GeV as factorization scale.", Q)

		sqrts := 14.0 * hep.TeV
		t.Logf("    using √s = %8.3f GeV.", sqrts)
		N := 100000
		t.Logf("    using N = %d monte carlo iterations", N)
		I, error := Sigma(neut, charg, sqrts*sqrts, Q, N, p)

		if math.Abs(I-tt.crossx) > 4.0*error {
			away := math.Abs(I-tt.crossx) / error
			t.Error("error: Calculated cross section not in 4 sigma interval of precalculated cross section.")
			t.Errorf("    calculated cross section: %8.3e +- %8.3e\n", I, error)
			t.Errorf("    expected cross section:   %8.3e\n", tt.crossx)
			t.Errorf("    %4.1f sigma away from precalculated result\n", away)
			continue
		} else {
			away := math.Abs(I-tt.crossx) / error
			t.Logf("    cross section = %8.3e +- %8.3e pb (%4.1f sigma away from precalculated result)\n", I, error, away)
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
	t.Logf("%d cross sections calculated: (1 cross section -> %3.1f %%)\n", lenp, 100.0/float64(lenp))
	t.Logf("    %4.2f %% in 1 sigma. (68.27 %% expected)\n", float64(onesigma)/float64(lenp)*100.0)
	t.Logf("    %4.2f %% in 2 sigma. (95.45 %% expected)\n", float64(twosigma)/float64(lenp)*100.0)
	t.Logf("    %4.2f %% in 3 sigma. (99.73 %% expected)\n", float64(threesigma)/float64(lenp)*100.0)
	if t.Failed() {
		t.Log("\nThere were results which were not in the 4 sigma interval.",
			"This is possible. Maybe you should rerun the test to see whether this happens again!")
	}
}

// test pp -> 𝜒_2^0 𝜒_1^+ with prospino results.
func TestSigma(t *testing.T) {
	testprecalc(1, 0, t, tests)
}

// test pp -> 𝜒_3^0 𝜒_1^+ with prospino results. 
// 𝜒_3^0 has negative mass!
func TestSigma2(t *testing.T) {
	testprecalc(2, 0, t, tests_20)
}
