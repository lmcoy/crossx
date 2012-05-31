package linalg

import (
	"fmt"
	"math"
)

// Matrix2 represents a 4 times 4 matrix in column major mode.
type Matrix2 [4]float64

// NewMatrix2 creates a new identity matrix.
func NewMatrix2() *Matrix2 {
	return &Matrix2{0: 1.0, 3: 1.0}
}

func (M *Matrix2) Copy() *Matrix2 {
	return &Matrix2{M[0], M[1], M[2], M[3]}
}

// At returns the component at position row, column.
func (M *Matrix2) At(row, column int) float64 {
	return M[row+2*column]
}

// Set sets the component at position row, column to value.
func (M *Matrix2) Set(row, column int, value float64) {
	M[row+2*column] = value
}

// Add adds A to M.
// M += A
func (M *Matrix2) Add(A *Matrix2) {
	M[0] += A[0]
	M[1] += A[1]
	M[2] += A[2]
	M[3] += A[3]
}

// Sub subtracts A from M.
// M -= A
func (M *Matrix2) Sub(A *Matrix2) {
	M[0] -= A[0]
	M[1] -= A[1]
	M[2] -= A[2]
	M[3] -= A[3]
}

// Mul multiplies M with  A.
// M *= A
func (M *Matrix2) Mul(A *Matrix2) {
	// prefetch values
	a11 := A[0]
	a12 := A[2]
	a21 := A[1]
	a22 := A[3]

	m11 := M[0]
	m12 := M[2]
	m21 := M[1]
	m22 := M[3]

	M[0] = a11*m11 + m12*a21
	M[1] = m21*a11 + m22*a21
	M[2] = m11*a12 + m12*a22
	M[3] = m21*a12 + m22*a22
}

// MulFactor multiplies M with factor.
// M *= factor
func (M *Matrix2) MulFactor(factor float64) {
	M[0] *= factor
	M[1] *= factor
	M[2] *= factor
	M[3] *= factor
}

// Det returns the determinant of the matrix.
func (M *Matrix2) Det() float64 {

	return M[0]*M[3] - M[1]*M[2]
}

// Inverted returns the inverse of the matrix.
// Returns identity matrix,false if M is not invertible.
func (M *Matrix2) Inverted() (inverse *Matrix2, ok bool) {
	a := M[0]
	b := M[2]
	c := M[1]
	d := M[3]

	// calculate determinant
	det := M.Det()
	if compareFloat64(det, 0.0) {
		return NewMatrix2(), false
	}

	inverse = &Matrix2{
		d / det,
		-c / det,
		-b / det,
		a / det}

	return inverse, true
}

// Transposed returns M transposed.
func (M *Matrix2) Transposed() *Matrix2 {
	return &Matrix2{
		M[0], M[2], M[1], M[3]}
}

// Returns true if M equals A otherwise false.
// Uses approximate equals not == operator.
func (M *Matrix2) Equals(A *Matrix2) bool {
	for i := 0; i < 4; i++ {
		if !compareFloat64(M[i], A[i]) {
			return false
		}
	}
	return true
}

// Column returns a new Vector2D with the column of the matrix M.
func (M *Matrix2) Column(c int) *Vector2D {
	return &Vector2D{M[2*c], M[2*c+1]}
}

// Row returns a new Vector2D with the row of the matrix M.
func (M *Matrix2) Row(r int) *Vector2D {
	return &Vector2D{M[r], M[r+2]}
}

// SetColumn sets the column c to the values of the Vector2D v.
func (M *Matrix2) SetColumn(c int, v *Vector2D) {
	M[2*c] = v[0]
	M[2*c+1] = v[1]
}

// SetRow sets the row r to the values of the Vector4D v.
func (M *Matrix2) SetRow(r int, v *Vector2D) {
	M[r] = v[0]
	M[r+2] = v[1]
}

// TimesVector returns the result of the matrix-vector product M * v.
func (M *Matrix2) TimesVector(v *Vector2D) *Vector2D {
	return &Vector2D{
		M[0]*v[0] + M[2]*v[1],
		M[1]*v[0] + M[3]*v[1]}
}

// Times returns the result of the matrix matrix multiplication M * A.
func (M *Matrix2) Times(A *Matrix2) *Matrix2 {
	result := M.Copy()
	result.Mul(A)
	return result
}

// Plus returns a new matrix with the result of M + A.
func (M *Matrix2) Plus(A *Matrix2) *Matrix2 {
	return &Matrix2{M[0] + A[0],
		M[1] + A[1],
		M[2] + A[2],
		M[3] + A[3]}
}

// Minus returns a new matrix with the result of M - A.
func (M *Matrix2) Minus(A *Matrix2) *Matrix2 {
	return &Matrix2{M[0] - A[0],
		M[1] - A[1],
		M[2] - A[2],
		M[3] - A[3]}
}

// TimesFactor returns a new matrix with the result factor * M.
func (M *Matrix2) TimesFactor(factor float64) *Matrix2 {
	return &Matrix2{M[0] * factor,
		M[1] * factor,
		M[2] * factor,
		M[3] * factor}
}

// String returns a string representation of the matrix M in one line.
func (M *Matrix2) String() string {
	return fmt.Sprintf("( %8.3f %8.3f | %8.3f %8.3f )",
		M[0], M[1], M[2], M[3])
}

// String returns a string representation of the matrix M in one line.
func (M *Matrix2) MultilineString() string {
	return fmt.Sprintf("( %8.3f %8.3f )\n( %8.3f %8.3f )",
		M[0], M[2], M[1], M[3])
}

func (M *Matrix2) IsDiagonal() bool {
	if !compareFloat64(M[1], 0.0) {
		return false
	}
	if !compareFloat64(M[2], 0.0) {
		return false
	}
	return true
}

func (M *Matrix2) QRDecomposition() (Q, R *Matrix2) {
	Q = NewMatrix2()
	R = NewMatrix2()

	e := [2]*Vector2D{}
	a := [2]*Vector2D{M.Column(0), M.Column(1)}
	e[0] = a[0].Normalized()

	e[1] = SubVector2D(a[1], e[0].TimesFactor(a[1].Dot(e[0]))).Normalized()

	for i := 0; i < 2; i++ {
		for j := i; j < 2; j++ {
			R.Set(i, j, a[j].Dot(e[i]))
		}
	}

	Q.SetColumn(0, e[0])
	Q.SetColumn(1, e[1])

	return
}

// Eigen returns a vector with all eigenvalues of this matrix and
// a matrix with the eigenvectors.
func (M *Matrix2) Eigen() (values *Vector2D, vectors *Matrix2) {
	Q, R := M.QRDecomposition()

	A := R.Times(Q)
	vectors = Q.Copy()
	for i := 0; i < 1000; i++ {
		Q, R = A.QRDecomposition()
		A = R.Times(Q)
		vectors.Mul(Q)
		if A.IsDiagonal() {
			break
		}
	}

	values = &Vector2D{A[0], A[3]}
	return
}

func (M *Matrix2) OrthonormalizeColumns() (basis *Matrix2) {
	u1 := M.Column(0)
	u2 := M.Column(1)
	proj := u2.Dot(u1) / u1.Dot(u1)
	u2.Sub(u1.TimesFactor(proj))

	basis = NewMatrix2()
	basis.SetColumn(0, u1.Normalized())
	basis.SetColumn(1, u2.Normalized())
	return
}

func (M *Matrix2) SingularValueDecomposition() (U, V *Matrix2, values *Vector2D) {
	U = NewMatrix2()
	V = NewMatrix2()

	// Calculate eigenvalues and vectors of M.M^T
	A := M.Times(M.Transposed())
	evalues, evectors := A.Eigen()
	if evalues[0] < evalues[1] {
		U.SetColumn(0, evectors.Column(0))
		U.SetColumn(1, evectors.Column(1))
	} else {
		U.SetColumn(0, evectors.Column(1))
		U.SetColumn(1, evectors.Column(0))
	}
	U = U.OrthonormalizeColumns()

	// Calculate eigenvalues and vectors of M^T.M
	B := M.Transposed().Times(M)
	evalues, evectors = B.Eigen()
	if evalues[0] < evalues[1] {
		V.SetColumn(0, evectors.Column(0))
		V.SetColumn(1, evectors.Column(1))
		values = &Vector2D{math.Sqrt(evalues[0]), math.Sqrt(evalues[1])}
	} else {
		V.SetColumn(0, evectors.Column(1))
		V.SetColumn(1, evectors.Column(0))
		values = &Vector2D{math.Sqrt(evalues[1]), math.Sqrt(evalues[0])}
	}
	V = V.OrthonormalizeColumns()

	return
}
