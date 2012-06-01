package integrator

import (
	"testing"
	"math"
	"time"
	"math/rand"
)

func TestIntegrate( t *testing.T ) {
	rand.Seed(time.Now().Unix())
	integrand := func(x float64) float64 {
		return math.Sin(x)*x
	}
	
	I, error := Integrate( integrand, 0.0, math.Pi, 100000 )
	
	if math.Abs(I - math.Pi) > 5.0*error {
		t.Errorf( "Result is more than 5 sigma from expected result away:\n\tResult: Integrate( sin(x)*x, 0, Pi ) = %f +- %f\n\tExpected: Pi (= %f)\n", I, error, math.Pi )
	}
}