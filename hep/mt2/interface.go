// Package mt2 implements the "Cambridge MT2 Variable".
//
// For more information about MT2 see
//     - http://arxiv.org/abs/hep-ph/9906349
//     - http://arxiv.org/abs/hep-ph/0304226
//
// This package uses mt2_bisect by Hsin-Chia Cheng and Zhenyu Han in version 1.01a.
// See http://particle.physics.ucdavis.edu/hefti/projects/doku.php?id=wimpmass for more
// information.
package mt2

import (
	. "physics/hep/mt2/mt2_bisect"
)

// MT2 returns the "Cambridge MT2 Variable" ("Stransverse Mass")
//
// Parameter:
//     massA    mass of particle A
//     pTA      x,y component of transverse momentum of particle A (len(pTA)==2)
//     massB    mass of particle B
//     pTB      x,y component of transverse momentum of particle B (len(pTB)==2)
//     m        mass of invisible particle
//     pTMissing x,y component of transverse momentum (len(pTMissing)==2)
//
// If any mass is < 0.0 or len of momenta doesn't equal 2 this function will panic.
//
// See: 
//     - http://arxiv.org/abs/hep-ph/9906349
//     - http://arxiv.org/abs/hep-ph/0304226
// for a detailed discussion.
func MT2(massA float64, pTA []float64, massB float64, pTB []float64, m float64, pTMissing []float64) float64 {
	if len(pTA) != 2 {
		panic("transverse momentum pTA must have two components: x, y!")
	}
	if len(pTB) != 2 {
		panic("transverse momentum pTB must have two components: x, y!")
	}
	if len(pTMissing) != 2 {
		panic("transverse momentum pTMissing must have two components: x, y!")
	}
	if massA < 0.0 {
		panic("massA must be >= 0.0")
	}
	if massB < 0.0 {
		panic("massB must be >= 0.0")
	}
	if m < 0.0 {
		panic("m must be >= 0.0")
	}
	pA := New_doubleArray(3)
	DoubleArray_setitem(pA, 0, massA)
	DoubleArray_setitem(pA, 1, pTA[0])
	DoubleArray_setitem(pA, 2, pTA[1])

	pB := New_doubleArray(3)
	DoubleArray_setitem(pB, 0, massB)
	DoubleArray_setitem(pB, 1, pTB[0])
	DoubleArray_setitem(pB, 2, pTB[1])

	pTMiss := New_doubleArray(3)
	DoubleArray_setitem(pTMiss, 0, 0.0)
	DoubleArray_setitem(pTMiss, 1, pTMissing[0])
	DoubleArray_setitem(pTMiss, 2, pTMissing[1])

	mt2 := NewMt2()
	mt2.Set_momenta(pA, pB, pTMiss)
	mt2.Set_mn(m)

	result := mt2.Get_mt2()

	Delete_doubleArray(pA)
	Delete_doubleArray(pB)
	Delete_doubleArray(pTMiss)
	DeleteMt2(mt2)

	return result
}
