// Package integrator provides functions for Monte Carlo Integration.
package integrator

import (
	"math"
	"math/rand"
)

type Integrator interface {
	Integrate( func(float64)float64, float64, float64, int ) (float64, float64)
}

// Random represents a random number generator.
type Random interface {
	// Distribution of the random number generator.
	Distribution( float64 ) float64
	// Generates random numbers.
	Rand() float64
}

// Uniform generates uniformly distributed random numbers in [A,B]
type Uniform struct {
	A,B float64
}

// Distribution returns the value of the uniform probabiltiy distribution at x.
//
// 	f(x) = 1.0/(B-A) for x in [A,B] otherwise 0
func (u *Uniform) Distribution( x float64 ) float64 {
	if x >= u.A && x < u.B {
		return 1.0/(u.B-u.A)
	}
	return 0.0
}

// Rand returns uniformly distributed random numbers in the interval [A,B]
func (u *Uniform) Rand() float64 {
	return (u.B-u.A)*rand.Float64()+u.A
}

// Integrate integrates the 1-dimensional function between a and b with Monte Carlo methods.
//
// This function uses N uniformly distributed random numbers to perform the integration.
func Integrate( f func(float64)float64, a, b float64, N int ) (I float64, error float64) {
	I2 := 0.0
	uniform := &Uniform{ A: a, B: b }
	// Integral ausrechnen mit:
        // I = (b-a)/N*sum_{i=1}^{N} f(x_i),
        // wobei x_i gleichverteilte Zufallszahlen im Intervall [a,b) sind.
	for i := 0; i < N; i++ {
		// Zufallszahl erzeugen und Funktionswert berechnen.
		fx := f( uniform.Rand() )
		I += fx
		I2 += fx*fx // Benötigt zur Berechnung des Fehlers V(X) = E(X^2)-E(X)^2
	}
	I *= (b-a)/float64(N)
	I2 *= (b-a)*(b-a)

	// Fehler auf den Integralwert berechnen.
	error = math.Sqrt( 1.0/(float64(N)-1.0)*( I2-float64(N)*I*I ) )/math.Sqrt(float64(N))
	return
}

func Integrate3( f func(float64,float64,float64) float64, lower []float64, upper []float64, N int ) (I float64, error float64) {
	I2 := 0.0
	uniform1 := &Uniform{ A: lower[0], B: upper[0] }
	uniform2 := &Uniform{ A: lower[1], B: upper[1] }
	uniform3 := &Uniform{ A: lower[2], B: upper[2] }
	
	for i := 0; i < N; i++ {
		x := uniform1.Rand()
		y := uniform2.Rand()
		z := uniform3.Rand()
		fx := f( x, y, z )
		I += fx
		I2 += fx*fx
	}
	V := 1.0
	for i := 0; i < len(lower); i++ {
		V *= (upper[i]-lower[i])
	}
	I *= V/float64(N)
	I2 *= V*V
	error = math.Sqrt( 1.0/(float64(N)-1.0)*( I2-float64(N)*I*I ) )/math.Sqrt(float64(N))
	return
}