package integrator

import (
	"math"
	"math/rand"
	"testing"
	"time"
)

func init() {
	rand.Seed(time.Now().Unix())
}

func TestIntegrate(t *testing.T) {
	rand.Seed(time.Now().Unix())
	integrand := func(x float64) float64 {
		return math.Sin(x) * x
	}

	I, error := Integrate(integrand, 0.0, math.Pi, 100000)

	if math.Abs(I-math.Pi) > 5.0*error {
		t.Errorf("Result is more than 5 sigma from expected result away:\n\tResult: Integrate( sin(x)*x, 0, Pi ) = %f +- %f\n\tExpected: Pi (= %f)\n", I, error, math.Pi)
	}
}

func TestIntegrate3(t *testing.T) {
	// Number of monte carlo iterations for each test
	N := 1000000

	// Calculate volume of a sphere with integration over spherical coordinates
	integrand := func(r, theta, phi float64) float64 {
		return r * r * math.Sin(theta)
	}

	R := 10.0 // Radius of the sphere
	lower := []float64{0.0, 0.0, 0.0}
	upper := []float64{R, math.Pi, 2.0 * math.Pi}

	I, error := Integrate3(integrand, lower, upper, N)
	expectedI := 4.0 / 3.0 * math.Pi * R * R * R // precalculated Result: 4/3*Pi*R^3

	if math.Abs(I-expectedI) > 5.0*error {
		t.Errorf("Calculating volume of a sphere with radius %4.2f...", R)
		t.Error(" Result is more than 5 sigma from expected result away:")
		t.Errorf("    Result: %8.3f +- %8.3f\n", I, error)
		t.Errorf("    Expected: %8.3f\n", expectedI)
	}

	// Calculate volume of a cylinder with integration over spherical coordinates
	integrand_cyl := func(h, z, phi float64) float64 {
		return z
	}

	R_cyl := math.E   // Radius of the cylinder
	H_cyl := math.Phi // Height of the cylinder
	lower_cyl := []float64{0.0, 0.0, 0.0}
	upper_cyl := []float64{H_cyl, R_cyl, 2.0 * math.Pi}

	I_cyl, error_cyl := Integrate3(integrand_cyl, lower_cyl, upper_cyl, N)
	expectedI_cyl := math.Pi * H_cyl * R_cyl * R_cyl

	if math.Abs(I_cyl-expectedI_cyl) > 5.0*error_cyl {
		t.Errorf("Calculating volume of a cylinder with radius %4.2f and height %4.2f...", R_cyl, H_cyl)
		t.Error(" Result is more than 5 sigma from expected result away:")
		t.Errorf("    Result: %8.3f +- %8.3f\n", I_cyl, error_cyl)
		t.Errorf("    Expected: %8.3f\n", expectedI_cyl)
	}

}
