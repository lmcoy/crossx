package linalg

import (
	"math"
)

const (
	epsilon = 1.0e-10
)

// compareFloat64 returns true iff a equals b.
//
// Two floating point numbers are assumed to be equal if 
// 	absolute error |a-b| < 1e-10
// 	relative error < 1e-10
//
// compareFloat64(a,b) == compareFloat64(b,a)
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
	if a == b {
		return true
	}
	// check absolute error
	if math.Abs(a-b) < epsilon {
		return true
	}
	// check relative error
	// do this since an error of 1 is very large for a value near 0
	// but it is small enough to assume two values to be equal
	// if the values are really large.
	var relError float64
	// use two cases two ensure that compareFloat64(a,b) == compareFloat64(b,a) in any case.
	if math.Abs(b) > math.Abs(a) {
		relError = math.Abs((a - b) / b)
	} else {
		relError = math.Abs((a - b) / a)
	}
	if relError <= epsilon {
		return true
	}
	return false
}

func compareComplex128(a, b complex128) bool {
	if a == b {
		return true
	}
	return compareFloat64(imag(a), imag(b)) && compareFloat64(real(a), real(b))
}
