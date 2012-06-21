package hep

import (
	"math"
	"physics/math/linalg"
)

const (
	// All values are given in GeV
	GeV = 1.0
	MeV = 1.0e-3
	KeV = 1.0e-6
	TeV = 1.0e+3
	// Converts a cross section in 1/GeV² to pb
	// Usage: s[pb] = s[1/GeV²]*CrossSectionToPb
	CrossSectionToPb = 3.8937944929e8
)

const (
	// sin(𝜃w)²
	Sw2   = 0.2312
	Alpha = 1.0 / 127.934
	//Alpha = 1.0 / 137.0
	// Z boson mass
	Mz = 91.1876 * GeV
	// W boson mass
	Mw = 80.385 * GeV
	// electron mass
	Me = 0.510998928 * MeV
	// proton mass
	Mp = 0.93827204 * GeV
	// neutron mass
	Mn = 939.565378 * MeV
	// charged pion mass
	Mpi = 139.57018 * MeV
	// pion mass
	Mpi0 = 134.9766 * MeV
)

var sw = math.Sqrt(Sw2)
var cw = math.Cos(math.Asin(sw))

// NeutralinoMassMatrix returns the mass matrix for neutralinos with the SUSY parameters in susy.
//
// 	mass matrix (symmetric):
// 		( M_bino,     0,      -cos(𝛽)*sw*Mz,   sin(𝛽)*sw*Mz ) 
// 		(    0,    M_wino,     cos(𝛽)*cw*Mz,  -sin(𝛽)*cw*Mz )
// 		(    *,       *,             0,             -µ      )
// 		(    *,       *,            -µ,              0      )
func NeutralinoMassMatrix(M_bino, M_wino, Mu, TanBeta float64) (m *linalg.Matrix4) {
	m = linalg.NewMatrix4()
	sb := math.Sin(math.Atan(TanBeta))
	cb := math.Cos(math.Atan(TanBeta))

	// precalculate values
	A := -cb * sw * Mz
	B := sb * sw * Mz
	C := cb * cw * Mz
	D := -sb * cw * Mz
	m.Set(0, 0, M_bino)
	m.Set(0, 1, 0.0)
	m.Set(0, 2, A)
	m.Set(0, 3, B)
	m.Set(1, 0, 0.0)
	m.Set(1, 1, M_wino)
	m.Set(1, 2, C)
	m.Set(1, 3, D)
	m.Set(2, 0, A)
	m.Set(2, 1, C)
	m.Set(2, 2, 0.0)
	m.Set(2, 3, -Mu)
	m.Set(3, 0, B)
	m.Set(3, 1, D)
	m.Set(3, 2, -Mu)
	m.Set(3, 3, 0.0)
	return
}

// CharginoMassMatrix returns the 2x2 chargino mass matrix.
//
//	M =
// 		( M_wino,        √2*Mw*cos(𝛽) )
// 		( √2*Mw*sin(𝛽),       µ       )
func CharginoMassMatrix(M_bino, M_wino, Mu, TanBeta float64) (m *linalg.Matrix2) {
	m = linalg.NewMatrix2()
	sb := math.Sin(math.Atan(TanBeta))
	cb := math.Cos(math.Atan(TanBeta))

	m.Set(0, 0, M_wino)
	m.Set(0, 1, math.Sqrt2*Mw*cb)
	m.Set(1, 0, math.Sqrt2*Mw*sb)
	m.Set(1, 1, Mu)
	return
}

// Heaviside returns 0.0 if x < 0 and 1.0 otherwise.
func Heaviside(x float64) float64 {
	if x < 0.0 {
		return 0.0
	}
	return 1.0
}
