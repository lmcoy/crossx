package integrator

import (
	"math"
	"math/rand"
)

type Integrator interface {
	Integrate( func(float64)float64, float64, float64, int ) (float64, float64)
}

type Random interface {
	Distribution( float64 ) float64
	Rand() float64
}

type Uniform struct {
	a,b float64
}

func (u *Uniform) Distribution( x float64 ) float64 {
	if x >= u.a && x < u.b {
		return 1.0/(u.b-u.a)
	}
	return 0.0
}

func (u *Uniform) Rand() float64 {
	return (u.b-u.a)*rand.Float64()+u.a
}

func Integrate( f func(float64)float64, a, b float64, N int ) (I float64, error float64) {
	I2 := 0.0
	uniform := &Uniform{ a: a, b: b }
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
	uniform1 := &Uniform{ a: lower[0], b: upper[0] }
	uniform2 := &Uniform{ a: lower[1], b: upper[1] }
	uniform3 := &Uniform{ a: lower[2], b: upper[2] }
	
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