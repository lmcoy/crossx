package math3d

import (
	"fmt"
	"math/cmplx"
)

// Vector4c represents a vector with four real components.
type Vector4c [4]complex128

func (v *Vector4c) Copy() *Vector4c {
	return &Vector4c{v[0], v[1], v[2], v[3]}
}

// Add adds the vector other to v.
func (v *Vector4c) Add(other *Vector4c) {
	v[0] += other[0]
	v[1] += other[1]
	v[2] += other[2]
	v[3] += other[3]
}

// Sub subtracts vector other from v.
func (v *Vector4c) Sub(other *Vector4c) {
	v[0] -= other[0]
	v[1] -= other[1]
	v[2] -= other[2]
	v[3] -= other[3]
}

// Mul multiplies every component of v with factor.
func (v *Vector4c) Mul(factor complex128) {
	v[0] *= factor
	v[1] *= factor
	v[2] *= factor
	v[3] *= factor
}

/*
// LengthSquared returns the squared euclidean length of v.
func (v *Vector4c) LengthSquared() complex128 {
	return v[0]*v[0] + v[1]*v[1] + v[2]*v[2] + v[3]*v[3]
}

// Length returns the euclidean length of v.
func (v *Vector4c) Length() complex128 {
	return math.Sqrt(v.LengthSquared())
}*/

// Sums all given vectors up.
func SumVector4c(first *Vector4c, others ...*Vector4c) *Vector4c {
	result := first.Copy()
	for _, vector := range others {
		result.Add(vector)
	}
	return result
}

// Subtracts all vectors form first.
func SubVector4c(first *Vector4c, others ...*Vector4c) *Vector4c {
	result := first.Copy()
	for _, vector := range others {
		result.Sub(vector)
	}
	return result
}

// Dot returns the dot product of l and r.
func (v *Vector4c) Dot(r *Vector4c) complex128 {
	return v[0]*cmplx.Conj(r[0]) + v[1]*cmplx.Conj(r[1]) + v[2]*cmplx.Conj(r[2]) + v[3]*cmplx.Conj(r[3])
}

// Equals returns true if l equals r.
func (v *Vector4c) Equals(r *Vector4c) bool {
	return compareComplex128(v[0], r[0]) && compareComplex128(v[1], r[1]) && compareComplex128(v[2], r[2]) && compareComplex128(v[3], r[3])
}

// String returns a string representation of the vector.
func (v *Vector4c) String() string {
	return fmt.Sprintf("(%8.3f, %8.3f, %8.3f, %8.3f)", v[0], v[1], v[2], v[3])
}

// Normalize normalizes v
func (v *Vector4c) Normalize() {
	norm := cmplx.Sqrt(v.Dot(v))
	if compareComplex128(norm, 0.0) {
		return
	}
	v[0] /= norm
	v[1] /= norm
	v[2] /= norm
	v[3] /= norm
}

func (v *Vector4c) Normalized() (r *Vector4c) {
	r = v.Copy()
	r.Normalize()
	return
}

func (v *Vector4c) TimesFactor(factor complex128) *Vector4c {
	return &Vector4c{factor * v[0], factor * v[1], factor * v[2], factor * v[3]}
}

