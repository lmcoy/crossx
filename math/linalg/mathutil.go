package linalg

import (
	"math"
	"math/cmplx"
)

const (
	epsilon = 1.0e-14
)

// compareFloat64 returns true true iff a equals b.
// Two floating point numbers are assumed to be equal if the distance between their 
// floating point representations is less than 10 steps.
func compareFloat64(a, b float64) bool {
	/*if a == b {
		return true
	}
	min, max := 0.0, 0.0
	if a < b {
		min, max = a, b
	} else {
		min, max = b, a
	}

	// math.Nextafter 10 times
	r := 0.0
	switch {
	case min == 0:
		r = math.Float64frombits(1)
	case min > 0:
		r = math.Float64frombits(math.Float64bits(min) + 10)
	default:
		r = math.Float64frombits(math.Float64bits(min) - 10)
	}

	if r > max {
		return true
	}
	return false*/
	return math.Abs(a-b) < epsilon
}

func compareComplex128(a, b complex128) bool {
	if a == b {
		return true
	}
	return cmplx.Abs(a-b) < epsilon
}
