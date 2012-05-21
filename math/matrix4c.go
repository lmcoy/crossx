package math3d

import (
	"fmt"
	"math/cmplx"
)

// Matrix4c represents a 4 times 4 matrix in column major mode.
type Matrix4c [16]complex128

// NewMatrix4c creates a new identity matrix.
func NewMatrix4c() *Matrix4c {
	return &Matrix4c{0: 1.0, 5: 1.0, 10: 1.0, 15: 1.0}
}

// Copy returns a pointer to a new copy of matrix M.
func (M *Matrix4c) Copy() *Matrix4c {
	return &Matrix4c{M[0], M[1], M[2], M[3], M[4], M[5], M[6], M[7], M[8], M[9], M[10], M[11], M[12], M[13], M[14], M[15]}
}

// At returns the component at position row, column.
func (M *Matrix4c) At(row, column int) complex128 {
	return M[row+4*column]
}

// Set sets the component at position row, column to value.
func (M *Matrix4c) Set(row, column int, value complex128) {
	M[row+4*column] = value
}

// Add adds A to M.
// M += A
func (M *Matrix4c) Add(A *Matrix4c) {
	M[0] += A[0]
	M[1] += A[1]
	M[2] += A[2]
	M[3] += A[3]
	M[4] += A[4]
	M[5] += A[5]
	M[6] += A[6]
	M[7] += A[7]
	M[8] += A[8]
	M[9] += A[9]
	M[10] += A[10]
	M[11] += A[11]
	M[12] += A[12]
	M[13] += A[13]
	M[14] += A[14]
	M[15] += A[15]
}

// Sub subtracts A from M.
// M -= A
func (M *Matrix4c) Sub(A *Matrix4c) {
	M[0] -= A[0]
	M[1] -= A[1]
	M[2] -= A[2]
	M[3] -= A[3]
	M[4] -= A[4]
	M[5] -= A[5]
	M[6] -= A[6]
	M[7] -= A[7]
	M[8] -= A[8]
	M[9] -= A[9]
	M[10] -= A[10]
	M[11] -= A[11]
	M[12] -= A[12]
	M[13] -= A[13]
	M[14] -= A[14]
	M[15] -= A[15]
}

// Mul multiplies M with  A.
// M *= A
func (M *Matrix4c) Mul(A *Matrix4c) {
	// prefetch values of the matrices.
	M00 := M[0]
	M10 := M[1]
	M20 := M[2]
	M30 := M[3]
	M01 := M[4]
	M11 := M[5]
	M21 := M[6]
	M31 := M[7]
	M02 := M[8]
	M12 := M[9]
	M22 := M[10]
	M32 := M[11]
	M03 := M[12]
	M13 := M[13]
	M23 := M[14]
	M33 := M[15]
	A00 := A[0]
	A10 := A[1]
	A20 := A[2]
	A30 := A[3]
	A01 := A[4]
	A11 := A[5]
	A21 := A[6]
	A31 := A[7]
	A02 := A[8]
	A12 := A[9]
	A22 := A[10]
	A32 := A[11]
	A03 := A[12]
	A13 := A[13]
	A23 := A[14]
	A33 := A[15]

	// perform calculation
	M[0] = M00*A00 + M01*A10 + M02*A20 + M03*A30
	M[4] = M00*A01 + M01*A11 + M02*A21 + M03*A31
	M[8] = M00*A02 + M01*A12 + M02*A22 + M03*A32
	M[12] = M00*A03 + M01*A13 + M02*A23 + M03*A33

	M[1] = M10*A00 + M11*A10 + M12*A20 + M13*A30
	M[5] = M10*A01 + M11*A11 + M12*A21 + M13*A31
	M[9] = M10*A02 + M11*A12 + M12*A22 + M13*A32
	M[13] = M10*A03 + M11*A13 + M12*A23 + M13*A33

	M[2] = M20*A00 + M21*A10 + M22*A20 + M23*A30
	M[6] = M20*A01 + M21*A11 + M22*A21 + M23*A31
	M[10] = M20*A02 + M21*A12 + M22*A22 + M23*A32
	M[14] = M20*A03 + M21*A13 + M22*A23 + M23*A33

	M[3] = M30*A00 + M31*A10 + M32*A20 + M33*A30
	M[7] = M30*A01 + M31*A11 + M32*A21 + M33*A31
	M[11] = M30*A02 + M31*A12 + M32*A22 + M33*A32
	M[15] = M30*A03 + M31*A13 + M32*A23 + M33*A33
}

// MulFactor multiplies M with factor.
// M *= factor
func (M *Matrix4c) MulFactor(factor complex128) {
	M[0] *= factor
	M[1] *= factor
	M[2] *= factor
	M[3] *= factor
	M[4] *= factor
	M[5] *= factor
	M[6] *= factor
	M[7] *= factor
	M[8] *= factor
	M[9] *= factor
	M[10] *= factor
	M[11] *= factor
	M[12] *= factor
	M[13] *= factor
	M[14] *= factor
	M[15] *= factor
}

// Det returns the determinant of the matrix.
func (M *Matrix4c) Det() complex128 {
	a0 := M[0]*M[5] - M[1]*M[4]
	a1 := M[0]*M[9] - M[8]*M[1]
	a2 := M[0]*M[13] - M[12]*M[1]
	a3 := M[4]*M[9] - M[8]*M[5]
	a4 := M[4]*M[13] - M[12]*M[5]
	a5 := M[8]*M[13] - M[12]*M[9]
	b0 := M[2]*M[7] - M[6]*M[3]
	b1 := M[2]*M[11] - M[10]*M[3]
	b2 := M[2]*M[15] - M[14]*M[3]
	b3 := M[6]*M[11] - M[10]*M[7]
	b4 := M[6]*M[15] - M[14]*M[7]
	b5 := M[10]*M[15] - M[14]*M[11]

	return a0*b5 - a1*b4 + a2*b3 + a3*b2 - a4*b1 + a5*b0
}

// Inverted returns the inverse of the matrix.
// Returns identity matrix,false if M is not invertible.
func (M *Matrix4c) Inverted() (inverse *Matrix4c, ok bool) {
	a0 := M[0]*M[5] - M[1]*M[4]
	a1 := M[0]*M[9] - M[8]*M[1]
	a2 := M[0]*M[13] - M[12]*M[1]
	a3 := M[4]*M[9] - M[8]*M[5]
	a4 := M[4]*M[13] - M[12]*M[5]
	a5 := M[8]*M[13] - M[12]*M[9]
	b0 := M[2]*M[7] - M[6]*M[3]
	b1 := M[2]*M[11] - M[10]*M[3]
	b2 := M[2]*M[15] - M[14]*M[3]
	b3 := M[6]*M[11] - M[10]*M[7]
	b4 := M[6]*M[15] - M[14]*M[7]
	b5 := M[10]*M[15] - M[14]*M[11]

	// calculate determinant
	det := a0*b5 - a1*b4 + a2*b3 + a3*b2 - a4*b1 + a5*b0
	if imag(det) < epsilon && imag(det) > -epsilon && real(det) < epsilon {
		return NewMatrix4c(), false
	}
	invDet := 1.0 / det
	inverse = &Matrix4c{
		(+M[5]*b5 - M[9]*b4 + M[13]*b3) * invDet,
		(-M[1]*b5 + M[9]*b2 - M[13]*b1) * invDet,
		(+M[1]*b4 - M[5]*b2 + M[13]*b0) * invDet,
		(-M[1]*b3 + M[5]*b1 - M[9]*b0) * invDet,
		(-M[4]*b5 + M[8]*b4 - M[12]*b3) * invDet,
		(+M[0]*b5 - M[8]*b2 + M[12]*b1) * invDet,
		(-M[0]*b4 + M[4]*b2 - M[12]*b0) * invDet,
		(+M[0]*b3 - M[4]*b1 + M[8]*b0) * invDet,
		(+M[7]*a5 - M[11]*a4 + M[15]*a3) * invDet,
		(-M[3]*a5 + M[11]*a2 - M[15]*a1) * invDet,
		(+M[3]*a4 - M[7]*a2 + M[15]*a0) * invDet,
		(-M[3]*a3 + M[7]*a1 - M[11]*a0) * invDet,
		(-M[6]*a5 + M[10]*a4 - M[14]*a3) * invDet,
		(+M[2]*a5 - M[10]*a2 + M[14]*a1) * invDet,
		(-M[2]*a4 + M[6]*a2 - M[14]*a0) * invDet,
		(+M[2]*a3 - M[6]*a1 + M[10]*a0) * invDet}

	return inverse, true
}

// Transposed returns M transposed.
func (M *Matrix4c) Transposed() *Matrix4c {
	return &Matrix4c{
		M[0], M[4], M[8], M[12],
		M[1], M[5], M[9], M[13],
		M[2], M[6], M[10], M[14],
		M[3], M[7], M[11], M[15]}
}

// Returns true if M equals A otherwise false.
// Uses approximate equals not == operator.
func (M *Matrix4c) Equals(A *Matrix4c) bool {
	for i := 0; i < 16; i++ {
		if !compareComplex128(M[i], A[i]) {
			return false
		}
	}
	return true
}

// Column returns a new Vector4c with the column of the matrix M.
func (M *Matrix4c) Column(c int) *Vector4c {
	return &Vector4c{M[4*c], M[4*c+1], M[4*c+2], M[4*c+3]}
}

// Row returns a new Vector4c with the row of the matrix M.
func (M *Matrix4c) Row(r int) *Vector4c {
	return &Vector4c{M[r], M[r+4], M[r+8], M[r+12]}
}

// SetColumn sets the column c to the values of the Vector4c v.
func (M *Matrix4c) SetColumn(c int, v *Vector4c) {
	M[4*c] = v[0]
	M[4*c+1] = v[1]
	M[4*c+2] = v[2]
	M[4*c+3] = v[3]
}

// SetRow sets the row r to the values of the Vector4c v.
func (M *Matrix4c) SetRow(r int, v *Vector4c) {
	M[r] = v[0]
	M[r+4] = v[1]
	M[r+8] = v[2]
	M[r+12] = v[3]
}

// TimesVector returns the result of the matrix-vector product M * v.
func (M *Matrix4c) TimesVector(v *Vector4c) *Vector4c {
	return &Vector4c{
		M[0]*v[0] + M[4]*v[1] + M[8]*v[2] + M[12]*v[3],
		M[1]*v[0] + M[5]*v[1] + M[9]*v[2] + M[13]*v[3],
		M[2]*v[0] + M[6]*v[1] + M[10]*v[2] + M[14]*v[3],
		M[3]*v[0] + M[7]*v[1] + M[11]*v[2] + M[15]*v[3]}
}

// Times returns the result of the matrix matrix multiplication M * A.
func (M *Matrix4c) Times(A *Matrix4c) *Matrix4c {
	return &Matrix4c{
		M[0]*A[0] + M[4]*A[1] + M[8]*A[2] + M[12]*A[3],
		M[1]*A[0] + M[5]*A[1] + M[9]*A[2] + M[13]*A[3],
		M[2]*A[0] + M[6]*A[1] + M[10]*A[2] + M[14]*A[3],
		M[3]*A[0] + M[7]*A[1] + M[11]*A[2] + M[15]*A[3],
		M[0]*A[4] + M[4]*A[5] + M[8]*A[6] + M[12]*A[7],
		M[1]*A[4] + M[5]*A[5] + M[9]*A[6] + M[13]*A[7],
		M[2]*A[4] + M[6]*A[5] + M[10]*A[6] + M[14]*A[7],
		M[3]*A[4] + M[7]*A[5] + M[11]*A[6] + M[15]*A[7],
		M[0]*A[8] + M[4]*A[9] + M[8]*A[10] + M[12]*A[11],
		M[1]*A[8] + M[5]*A[9] + M[9]*A[10] + M[13]*A[11],
		M[2]*A[8] + M[6]*A[9] + M[10]*A[10] + M[14]*A[11],
		M[3]*A[8] + M[7]*A[9] + M[11]*A[10] + M[15]*A[11],
		M[0]*A[12] + M[4]*A[13] + M[8]*A[14] + M[12]*A[15],
		M[1]*A[12] + M[5]*A[13] + M[9]*A[14] + M[13]*A[15],
		M[2]*A[12] + M[6]*A[13] + M[10]*A[14] + M[14]*A[15],
		M[3]*A[12] + M[7]*A[13] + M[11]*A[14] + M[15]*A[15]}
}

// Plus returns a new matrix with the result of M + A.
func (M *Matrix4c) Plus(A *Matrix4c) *Matrix4c {
	return &Matrix4c{M[0] + A[0],
		M[1] + A[1],
		M[2] + A[2],
		M[3] + A[3],
		M[4] + A[4],
		M[5] + A[5],
		M[6] + A[6],
		M[7] + A[7],
		M[8] + A[8],
		M[9] + A[9],
		M[10] + A[10],
		M[11] + A[11],
		M[12] + A[12],
		M[13] + A[13],
		M[14] + A[14],
		M[15] + A[15]}
}

// Minus returns a new matrix with the result of M - A.
func (M *Matrix4c) Minus(A *Matrix4c) *Matrix4c {
	return &Matrix4c{M[0] - A[0],
		M[1] - A[1],
		M[2] - A[2],
		M[3] - A[3],
		M[4] - A[4],
		M[5] - A[5],
		M[6] - A[6],
		M[7] - A[7],
		M[8] - A[8],
		M[9] - A[9],
		M[10] - A[10],
		M[11] - A[11],
		M[12] - A[12],
		M[13] - A[13],
		M[14] - A[14],
		M[15] - A[15]}
}

// TimesFactor returns a new matrix with the result factor * M.
func (M *Matrix4c) TimesFactor(factor complex128) *Matrix4c {
	return &Matrix4c{M[0] * factor,
		M[1] * factor,
		M[2] * factor,
		M[3] * factor,
		M[4] * factor,
		M[5] * factor,
		M[6] * factor,
		M[7] * factor,
		M[8] * factor,
		M[9] * factor,
		M[10] * factor,
		M[11] * factor,
		M[12] * factor,
		M[13] * factor,
		M[14] * factor,
		M[15] * factor}
}

// String returns a string representation (column major) of the matrix M in one line.
func (M *Matrix4c) String() string {
	return fmt.Sprintf("( %8.3f %8.3f %8.3f %8.3f | %8.3f %8.3f %8.3f %8.3f | %8.3f %8.3f %8.3f %8.3f | %8.3f %8.3f %8.3f %8.3f )",
		M[0], M[1], M[2], M[3], M[4], M[5], M[6], M[7], M[8], M[9], M[10], M[11], M[12], M[13], M[14], M[15])
}

// IsDiagonal returns true if M is a diagonal matrix. 
func (M *Matrix4c) IsDiagonal() bool {
	for i := 1; i < 15; i++ {
		if i == 5 || i == 10 { // Do not check diagonal elements
			i += 1
		}
		if !compareComplex128(M[i], 0.0) {
			return false
		}
	}
	return true
}

// IsIdentity returns true if M is an identity matrix.
func (M *Matrix4c) IsIdentity() bool {
	for i := 0; i < 4; i++ {
		for j := 0; j < 4; j++ {
			if i == j && compareComplex128(M.At(i, j), 1.0) == false {
				return false
			}
			if i != j && compareComplex128(M.At(i, j), 0.0) == false {
				return false
			}

		}
	}
	return true
}

// IsUpperTriangular returns true if M is an upper triangular matrix.
func (M *Matrix4c) IsUpperTriangular() bool {
	for row := 1; row < 4; row++ {
		for column := 0; column < row; column++ {
			r := M.At(row, column)
			if compareComplex128(r, 0.0) == false {
				return false
			}
		}
	}
	return true
}

// QRDecomposition returns the QR decomposition matrices Q and R of M.
func (M *Matrix4c) QRDecomposition() (Q, R *Matrix4c) {
	Q = NewMatrix4c()
	R = NewMatrix4c()

	e := [4]*Vector4c{}
	a := [4]*Vector4c{M.Column(0), M.Column(1), M.Column(2), M.Column(3)}

	e[0] = a[0].Normalized()

	e[1] = SubVector4c(a[1], e[0].TimesFactor(a[1].Dot(e[0]))).Normalized()

	e[2] = SubVector4c(a[2], e[0].TimesFactor(a[2].Dot(e[0])),
		e[1].TimesFactor(a[2].Dot(e[1]))).Normalized()

	e[3] = SubVector4c(a[3], e[0].TimesFactor(a[3].Dot(e[0])),
		e[1].TimesFactor(a[3].Dot(e[1])),
		e[2].TimesFactor(a[3].Dot(e[2]))).Normalized()

	for i := 0; i < 4; i++ {
		for j := i; j < 4; j++ {
			R.Set(i, j, a[j].Dot(e[i]))
		}
	}

	Q.SetColumn(0, e[0])
	Q.SetColumn(1, e[1])
	Q.SetColumn(2, e[2])
	Q.SetColumn(3, e[3])

	return
}

// Eigen returns a vector with all eigenvalues of this matrix and
// a matrix with the eigenvectors.
func (M *Matrix4c) Eigen() (values *Vector4c, vectors *Matrix4c) {
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

	values = &Vector4c{A[0], A[5], A[10], A[15]}

	for n := 4; n > 1; n-- {
		for k := 0; k < n-1; k++ {
			if cmplx.Abs(values[k]) > cmplx.Abs(values[k+1]) {
				values[k], values[k+1] = values[k+1], values[k]
				vectors.SwapColumns(k, k+1)
			}
		}
	}
	return
}

// SwapColumns swaps the columns i and j of M.
func (M *Matrix4c) SwapColumns(i, j int) {
	if i == j {
		return
	}
	tmp := M.Column(i)
	M.SetColumn(i, M.Column(j))
	M.SetColumn(j, tmp)
}

// SwapRows swaps the rows i and j of M.
func (M *Matrix4c) SwapRows(i, j int) {
	if i == j {
		return
	}
	tmp := M.Row(i)
	M.SetRow(i, M.Row(j))
	M.SetRow(j, tmp)
}

// MultilineString returns a string representation of M where every row is in a new line.
func (M *Matrix4c) MultilineString() string {
	return fmt.Sprintf("( %8.3f %8.3f %8.3f %8.3f )\n( %8.3f %8.3f %8.3f %8.3f )\n( %8.3f %8.3f %8.3f %8.3f )\n( %8.3f %8.3f %8.3f %8.3f )",
		M[0], M[4], M[8], M[12], M[1], M[5], M[9], M[13], M[2], M[6], M[10], M[14], M[3], M[7], M[11], M[15])
}
