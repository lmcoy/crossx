package mt2

import (
	"math"
	"testing"
)

const (
	epsilon = 1.0e-6
)

func TestMT2(t *testing.T) {
	mt2 := MT2(0.106, []float64{39.0, 12.0}, 0.106, []float64{119.0, -33.0}, 50.0, []float64{-29.9, 35.9})

	mt2_pre := 107.12787908729383
	if math.Abs(mt2-mt2_pre)/mt2_pre > epsilon {
		t.Errorf("mt2 == %f but mt2 == %f expected", mt2, mt2_pre)
	}
}
