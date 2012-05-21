package math3d

import (
	"fmt"
	"math"
)

// Vector2D represents a vector with four real components.
type Vector2D [2]float64

func (v *Vector2D) Copy() *Vector2D {
	return &Vector2D{v[0], v[1]}
}

// Add adds the vector other to v.
func (v *Vector2D) Add(other *Vector2D) {
	v[0] += other[0]
	v[1] += other[1]
}

// Sub subtracts vector other from v.
func (v *Vector2D) Sub(other *Vector2D) {
	v[0] -= other[0]
	v[1] -= other[1]
}

// Mul multiplies every component of v with factor.
func (v *Vector2D) Mul(factor float64) {
	v[0] *= factor
	v[1] *= factor
}

// LengthSquared returns the squared euclidean length of v.
func (v *Vector2D) LengthSquared() float64 {
	return v[0]*v[0] + v[1]*v[1]
}

// Length returns the euclidean length of v.
func (v *Vector2D) Length() float64 {
	return math.Sqrt(v.LengthSquared())
}

// Sums all given vectors up.
func SumVector2D(first *Vector2D, others ...*Vector2D) *Vector2D {
	result := first.Copy()
	for _, vector := range others {
		result.Add(vector)
	}
	return result
}

// Subtracts all vectors form first.
func SubVector2D(first *Vector2D, others ...*Vector2D) *Vector2D {
	result := first.Copy()
	for _, vector := range others {
		result.Sub(vector)
	}
	return result
}

// Dot returns the dot product of l and r.
func (v *Vector2D) Dot(r *Vector2D) float64 {
	return v[0]*r[0] + v[1]*r[1]
}

// Equals returns true if l equals r.
func (v *Vector2D) Equals(r *Vector2D) bool {
	return compareFloat64(v[0], r[0]) && compareFloat64(v[1], r[1])
}

// String returns a string representation of the vector.
func (v *Vector2D) String() string {
	return fmt.Sprintf("(%8.3f, %8.3f)", v[0], v[1])
}

// Normalize normalizes v
func (v *Vector2D) Normalize() {
	length := v.Length()
	if length == 0.0 {
		return
	}
	v[0] /= length
	v[1] /= length
}

func (v *Vector2D) Normalized() (r *Vector2D) {
	r = v.Copy()
	r.Normalize()
	return
}

func (v *Vector2D) TimesFactor(factor float64) *Vector2D {
	return &Vector2D{factor * v[0], factor * v[1]}
}
