package linalg

import (
	"math/rand"
	"testing"
)

// Global variables for tests
var A = &Matrix4{
	1.0, 0.0, 2.0, 2.0,
	0.0, 2.0, 1.0, 0.0,
	0.0, 1.0, 0.0, 1.0,
	1.0, 2.0, 1.0, 4.0}

var expInvA = &Matrix4{
	-2.0, 1.0, -8.0, 3.0,
	-0.5, 0.5, -1.0, 0.5,
	1.0, 0.0, 2.0, -1.0,
	0.5, -0.5, 2.0, -0.5}

var B = &Matrix4{
	2., 4., 3., 9.,
	231., 23., 25., 34.,
	-34.5, 3.5, -6.0, 2.0,
	14.5, -6., 1.5, 5.5}

var C = &Matrix4{
	3.5, 1.5, 5., -3.0,
	-2.5, 1., 23., 2.,
	5.5, -4.5, -4.0, 5.0,
	-3.0, -0.5, 6.5, -4.0}

var D = &Matrix4{
	1.000, 0.000, 1.000, 1.000,
	0.000, 1.000, 1.000, 1.000,
	1.000, 1.000, 0.000, 1.000,
	0.000, 0.000, 1.000, 0.000}

var expBtimesC = &Matrix4{
	137.500, 84.000, 13.500, 76.000,
	-538.500, 81.500, -117.500, 68.500,
	-818.000, -125.500, -64.500, -84.000,
	-403.750, 23.250, -66.500, -53.000}

var expCtimesB = &Matrix4{
	-13.500, -11.000, 148.500, -19.000,
	786.500, 240.000, 1805.000, -658.000,
	-168.500, -22.250, -55.000, 72.500,
	57.500, 6.250, -35.750, -70.000}

var expInvD = &Matrix4{
	0.000, -1.000, 1.000, 1.000,
	-1.000, 0.000, 1.000, 1.000,
	0.000, 0.000, 0.000, 1.000,
	1.000, 1.000, -1.000, -2.000}

var expTransA = &Matrix4{
	1.0, 0.0, 0.0, 1.0,
	0.0, 2.0, 1.0, 2.0,
	2.0, 1.0, 0.0, 1.0,
	2.0, 0.0, 1.0, 4.0}

// Global variables for benchmarks
var bA, bB Matrix4

// tests
func TestMul(t *testing.T) {
	b := B.Copy()
	b.Mul(C)
	if !b.Equals(expBtimesC) {
		t.Errorf("B *= C: \nB:        %v\nC:        %v\nExpected: %v\nResult:   %v", B, C, expBtimesC, b)
	}

	c := C.Copy()
	c.Mul(B)
	if !c.Equals(expCtimesB) {
		t.Errorf("C *= B: \nB:        %v\nC:        %v\nExpected: %v\nResult:   %v", B, C, expCtimesB, c)
	}
}

func TestTimes(t *testing.T) {
	a := B.Times(C)
	if !a.Equals(expBtimesC) {
		t.Errorf("B * C: \nB:        %v\nC:        %v\nExpected: %v\nResult:   %v", B, C, expBtimesC, a)
	}

	b := C.Times(B)
	if !b.Equals(expCtimesB) {
		t.Errorf("C * B: \nB:        %v\nC:        %v\nExpected: %v\nResult:   %v", B, C, expCtimesB, b)
	}
}

func TestInverse(t *testing.T) {
	invA, invertible := A.Inverted()
	if !invertible {
		t.Errorf("A^-1: Expected: %v is invertible! Result: Not invertible!", A)
	} else {
		if !invA.Equals(expInvA) {
			t.Errorf("A^-1: \nA:        %v\nExpected: %v\nResult:   %v", A, expInvA, invA)
		}
	}
	invD, _ := D.Inverted()
	if !invD.Equals(expInvD) {
		t.Errorf("D^-1: \nD:        %v\nExpected: %v\nResult:   %v", D, expInvD, invD)
	}
}

func TestTransposed(t *testing.T) {
	trans := A.Transposed()
	if !trans.Equals(expTransA) {
		t.Errorf("A^T: \nExpected: %v\nResult:   %v", expTransA, trans)
	}
}

func TestMulFactor(t *testing.T) {
	a := A.Copy()
	factor := rand.Float64()
	a.MulFactor(factor)

	for i := 0; i < 16; i++ {
		if !compareFloat64(a[i], A[i]*factor) {
			t.Errorf("A*factor:\n Expected: %v\nResult:   %v", A[i]*factor, a[i])
		}
	}
}

func TestTimesFactor(t *testing.T) {
	factor := rand.Float64()
	a := A.TimesFactor(factor)
	for i := 0; i < 16; i++ {
		if !compareFloat64(a[i], A[i]*factor) {
			t.Errorf("A*factor:\n Expected: %v\nResult:   %v", A[i]*factor, a[i])
		}
	}
}

func TestQRDecomposition(t *testing.T) {
	Q, R := A.QRDecomposition()

	q := Q.Times(Q.Transposed())
	if q.IsIdentity() == false {
		t.Errorf("Q must be orthogonal!\nQ = \n%s\nQ.Q^T = 1 expected but got\n%s", Q.MultilineString(), q.MultilineString())
	}

	if R.IsUpperTriangular() == false {
		t.Errorf("R must be an upper triangular matrix!\n But got:\nR =\n%s", R.MultilineString())
	}

	comp := Q.Times(R)
	if A.Equals(comp) == false {
		t.Errorf("Expected: Q.R == A\n Q = \n%s\nR = \n%s\nOriginal A =\n%s\nQ.R =\n%s",
			Q.MultilineString(), R.MultilineString(), A.MultilineString(), comp.MultilineString())
	}
}

func TestEigen(t *testing.T) {
	M := NewMatrix4()
	M.SetColumn(0, &Vector4D{1.0, 2.0, 1.0, 3.0})
	M.SetColumn(1, &Vector4D{2.0, 4.0, 5.0, 1.0})
	M.SetColumn(2, &Vector4D{1.0, 5.0, -1.0, 4.0})
	M.SetColumn(3, &Vector4D{3.0, 1.0, 4.0, -3.0})

	vals, vecs := M.Eigen()
	failed := false
	for i := 0; i < 4; i++ {
		lhs := M.TimesVector(vecs.Column(i))
		rhs := vecs.Column(i).TimesFactor(vals[i])
		if !lhs.Equals(rhs) {
			t.Logf("Value: %f, Vector: %s not Eigenvalue, Eigenvector of\n M = \n%s\n", vals[i], vecs.Column(i), M.MultilineString())
			failed = true
		}
	}
	if failed {
		t.Fail()
	}
}

// benchmarks
func SetupBenchmark() {
	for i, _ := range bA {
		bA[i] = rand.Float64()
		bB[i] = rand.Float64()
	}
}

func BenchmarkInverted(b *testing.B) {
	b.StopTimer()
	SetupBenchmark()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		bA.Inverted()
	}
}

func BenchmarkMul(b *testing.B) {
	b.StopTimer()
	SetupBenchmark()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		bA.Mul(&bB)
	}
}

func BenchmarkAdd(b *testing.B) {
	b.StopTimer()
	SetupBenchmark()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		bA.Add(&bB)
	}
}
