package linalg

import (
	"fmt"
	"math"
)

// Vector4D represents a vector with four real components.
type Vector4D [4]float64

func (v *Vector4D) Copy() *Vector4D {
	return &Vector4D{v[0], v[1], v[2], v[3]}
}

// Add adds the vector other to v.
func (v *Vector4D) Add(other *Vector4D) {
	v[0] += other[0]
	v[1] += other[1]
	v[2] += other[2]
	v[3] += other[3]
}

// Sub subtracts vector other from v.
func (v *Vector4D) Sub(other *Vector4D) {
	v[0] -= other[0]
	v[1] -= other[1]
	v[2] -= other[2]
	v[3] -= other[3]
}

// Mul multiplies every component of v with factor.
func (v *Vector4D) Mul(factor float64) {
	v[0] *= factor
	v[1] *= factor
	v[2] *= factor
	v[3] *= factor
}

// LengthSquared returns the squared euclidean length of v.
func (v *Vector4D) LengthSquared() float64 {
	return v[0]*v[0] + v[1]*v[1] + v[2]*v[2] + v[3]*v[3]
}

// Length returns the euclidean length of v.
func (v *Vector4D) Length() float64 {
	return math.Sqrt(v.LengthSquared())
}

// Sums all given vectors up.
func SumVector4D(first *Vector4D, others ...*Vector4D) *Vector4D {
	result := first.Copy()
	for _, vector := range others {
		result.Add(vector)
	}
	return result
}

// Subtracts all vectors form first.
func SubVector4D(first *Vector4D, others ...*Vector4D) *Vector4D {
	result := first.Copy()
	for _, vector := range others {
		result.Sub(vector)
	}
	return result
}

// Dot returns the dot product of l and r.
func (v *Vector4D) Dot(r *Vector4D) float64 {
	return v[0]*r[0] + v[1]*r[1] + v[2]*r[2] + v[3]*r[3]
}

// Equals returns true if l equals r.
func (v *Vector4D) Equals(r *Vector4D) bool {
	return compareFloat64(v[0], r[0]) && compareFloat64(v[1], r[1]) && compareFloat64(v[2], r[2]) && compareFloat64(v[3], r[3])
}

// String returns a string representation of the vector.
func (v *Vector4D) String() string {
	return fmt.Sprintf("(%8.3f, %8.3f, %8.3f, %8.3f)", v[0], v[1], v[2], v[3])
}

// Normalize normalizes v
func (v *Vector4D) Normalize() {
	length := v.Length()
	if length == 0.0 {
		return
	}
	v[0] /= length
	v[1] /= length
	v[2] /= length
	v[3] /= length
}

func (v *Vector4D) Normalized() (r *Vector4D) {
	r = v.Copy()
	r.Normalize()
	return
}

func (v *Vector4D) TimesFactor(factor float64) *Vector4D {
	return &Vector4D{factor * v[0], factor * v[1], factor * v[2], factor * v[3]}
}

func (v *Vector4D) ToVector3D() Vector3D {
	return Vector3D{v[0], v[1], v[2]}
}
