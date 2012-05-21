package math3d

import (
	"fmt"
	"math"
)

// Vector3D represents a vector with three real components.
type Vector3D [3]float64

// Add adds the vector other to this vector.
func (v *Vector3D) Add(other *Vector3D) {
	v[0] += other[0]
	v[1] += other[1]
	v[2] += other[2]
}

// Sub subtracts vector other from this vector.
func (v *Vector3D) Sub(other *Vector3D) {
	v[0] -= other[0]
	v[1] -= other[1]
	v[2] -= other[2]
}

// Mul multiplies every component with factor.
func (v *Vector3D) Mul(factor float64) {
	v[0] *= factor
	v[1] *= factor
	v[2] *= factor
}

// LengthSquared returns the squared euclidean length of the vector.
func (v *Vector3D) LengthSquared() float64 {
	return v[0]*v[0] + v[1]*v[1] + v[2]*v[2]
}

// Length returns the euclidean length of the vector.
func (v *Vector3D) Length() float64 {
	return math.Sqrt(v.LengthSquared())
}

// Sums all given vectors up.
func SumVector3D(first *Vector3D, others ...*Vector3D) Vector3D {
	result := *first
	for _, vector := range others {
		result.Add(vector)
	}
	return result
}

// Subtracts all vectors form first.
func SubVector3D(first *Vector3D, others ...*Vector3D) Vector3D {
	result := *first
	for _, vector := range others {
		result.Sub(vector)
	}
	return result
}

// Minus returns a new Vector3D with the result of v - o.
func (v *Vector3D) Minus(o *Vector3D) *Vector3D {
	return &Vector3D{v[0] - o[0], v[1] - o[1], v[2] - o[2]}
}

// Plus returns a new Vector3D with the result of v + o.
func (v *Vector3D) Plus(o *Vector3D) *Vector3D {
	return &Vector3D{v[0] + o[0], v[1] + o[1], v[2] + o[2]}
}

// Dot returns the dot product of v and l.
func (v *Vector3D) Dot(l *Vector3D) float64 {
	return l[0]*v[0] + l[1]*v[1] + l[2]*v[2]
}

// Cross returns the cross product of v and r.
func (v *Vector3D) Cross(r *Vector3D) *Vector3D {
	return &Vector3D{v[1]*r[2] - v[2]*r[1], v[2]*r[0] - v[0]*r[2], v[0]*r[1] - v[1]*r[0]}
}

// Equals returns true if every component of v equals the corresponding component of o.
func (v *Vector3D) Equals(o *Vector3D) bool {
	return compareFloat64(v[0], o[0]) && compareFloat64(v[1], o[1]) && compareFloat64(v[2], o[2])
}

// String returns a string representation of v.
func (v *Vector3D) String() string {
	return fmt.Sprintf("(%8.3f, %8.3f, %8.3f)", v[0], v[1], v[2])
}

// Normalize normalizes v, i.e. sets the length of this vector to 1.0.
func (v *Vector3D) Normalize() {
	length := v.Length()
	if length == 0.0 {
		return
	}
	v[0] /= length
	v[1] /= length
	v[2] /= length
}

// IsZero returns true iff all components of v are 0.0.
func (v *Vector3D) IsZero() bool {
	return compareFloat64(v[0], 0.0) && compareFloat64(v[1], 0.0) && compareFloat64(v[2], 0.0)
}

// ToVector4D returns v as 4D vector with the last component set to 0.0
func (v *Vector3D) ToVector4D() *Vector4D {
	return &Vector4D{v[0], v[1], v[2], 0.0}
}

// Times returns a new Vector3D with the result of factor * v.
func (v *Vector3D) Times(factor float64) *Vector3D {
	return &Vector3D{v[0] * factor, v[1] * factor, v[2] * factor}
}
