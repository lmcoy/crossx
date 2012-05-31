package linalg

import (
	"testing"
)

func TestCompareFloat64(t *testing.T) {
	if compareFloat64(2.0, 3.0) {
		t.Errorf("2.0 does not equal 3.0")
	}
	if !compareFloat64(2.0, 2.0) {
		t.Errorf("2.0 equals 2.0")
	}

	if compareFloat64(0.0, 1.0e-3) {
		t.Errorf("0.0 does not equal 1e-3")
	}
}

func BenchmarkCompareFloat64(b *testing.B) {
	for i := 0; i < b.N; i++ {
		compareFloat64(2.0, 2.0+1e-15)
	}
}
