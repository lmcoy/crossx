package kinematics

import (
	"math"
)

// Mandelstam_t calculates t for a given value of cos𝜃.
//
// m3,m4: masses of the outgoing particles.
func Mandelstam_t(cos_theta, s, m3, m4 float64) float64 {
	m3_2 := m3 * m3
	m3_4 := m3_2 * m3_2
	m4_2 := m4 * m4
	p_prime := math.Sqrt((m3_4-2*m3_2*(m4_2+s)+(m4_2-s)*(m4_2-s))/s) / 2.0
	E3 := math.Sqrt(m3_2 + p_prime*p_prime)

	return m3_2 + math.Sqrt(s)*(p_prime*cos_theta-E3)
}
