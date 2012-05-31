package linalg

import (
	"testing"
)

func TestCrossProduct(t *testing.T) {
	// input
	a := &Vector3D{1.0, 2.0, 3.0}
	b := &Vector3D{-7.0, 8.0, 9.0}

	// expected results
	exp_a_x_b := &Vector3D{-6.0, -30.0, 22.0}

	// Test
	a_x_b := a.Cross(b)
	if !a_x_b.Equals(exp_a_x_b) {
		t.Errorf("cross product: \nExpected: %v\nResult:   %v", exp_a_x_b, a_x_b)
	}
}

func TestDot(t *testing.T) {
	// input
	a := &Vector3D{1.0, 3.0, -5.0}
	b := &Vector3D{4.0, -2.0, -1.0}

	// expected results
	exp_a_dot_b := 3.0

	// test
	a_dot_b := a.Dot(b)
	if !compareFloat64(a_dot_b, exp_a_dot_b) {
		t.Errorf("dot product: \nExpected: %v\nResult:   %v", exp_a_dot_b, a_dot_b)
	}
}
