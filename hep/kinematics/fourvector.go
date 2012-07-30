package kinematics

import (
	"math"
	"physics/math/linalg"
)

// FourVector represents a 4 vector.
type FourVector [4]float64

// NewFourVector constructs a new four vector.
func NewFourVector(x0, x1, x2, x3 float64) *FourVector {
	return &FourVector{x0, x1, x2, x3}
}

// NewFourVectorFromMomentumAndMass constructs a four vector from momentum p
// and mass m.
func NewFourVectorFromMomentumAndMass(m, p1, p2, p3 float64) *FourVector {
	return &FourVector{
		math.Sqrt(p1*p1 + p2*p2 + p3*p3 + m*m),
		p1,
		p2,
		p3,
	}
}

// NewFourVectorFromPtEtaPhiE constructs a four vector from pseudorapidity eta,
// azimuthal angle phi, transverse momentum pT and energy E.
func NewFourVectorFromPtEtaPhiE(e, pT, eta, phi float64) *FourVector {
	pt := math.Abs(pT)
	return &FourVector{
		e,
		pt * math.Cos(phi),
		pt * math.Sin(phi),
		pt * math.Sinh(eta),
	}
}

// NewFourVectorFromPtEtaPhiM constructs a four vector from mass m,
// transverse momentum pT, pseudorapidity eta, azimuthal angle phi.
func NewFourVectorFromPtEtaPhiM(m, pT, eta, phi float64) *FourVector {
	pt := math.Abs(pT)
	return NewFourVectorFromMomentumAndMass(m, pt*math.Cos(phi), pt*math.Sin(phi), pt*math.Sinh(eta))
}

// Phi returns the azimuthal angle in the range [-π,π].
//
// For an angle in [0,2π] add 2π to the negative values.
func (fv *FourVector) Phi() float64 {
	return math.Atan2(fv[2], fv[1])
}

// Theta returns the polar angle in the range [0:π].
func (fv *FourVector) Theta() float64 {
	tmp := math.Sqrt(fv[1]*fv[1] + fv[2]*fv[2])
	return math.Atan2(tmp, fv[3])
}

// PseudoRapidity returns the pseudorapidity.
func (fv *FourVector) PseudoRapidity() float64 {
	return math.Log(math.Tan(fv.Theta() / 2.0))
}

// ThreeVectorAbs returns the length of the spatial components, i.e.
//     px²+py²+pz²
func (fv *FourVector) ThreeVectorAbs() float64 {
	return math.Sqrt(fv[1]*fv[1] + fv[2]*fv[2] + fv[3]*fv[3])
}

// E returns the Energy of this four vector, i.e. the x^0 component.
func (fv *FourVector) E() float64 {
	return fv[0]
}

// ThreeVector returns the spatial part of the four vector.
func (fv *FourVector) ThreeVector() linalg.Vector3D {
	return linalg.Vector3D{0: fv[1], 1: fv[2], 2: fv[3]}
}

// PT returns the transverse momentum.
//
// transverse momentum:
//     Sqrt(px*px + py*py)
func (fv *FourVector) PT() float64 {
	return math.Sqrt(fv[1]*fv[1] + fv[2]*fv[2])
}

// ET returns the transverse energy.
//
//     ET = E*sin(theta) = E*PT/|P|
func (fv *FourVector) ET() float64 {
	return fv.E() * fv.PT() / fv.ThreeVectorAbs()
}

// Dot caclulate the four vector dot product of fv and fv2
func (fv *FourVector) Dot(fv2 *FourVector) float64 {
	return fv[0]*fv2[0] - fv[1]*fv2[1] - fv[2]*fv2[2] - fv[3]*fv2[3]
}

// Plus returns a new FourVector fv + fv2.
func (fv *FourVector) Plus(fv2 *FourVector) *FourVector {
	return &FourVector{fv[0] + fv2[0], fv[1] + fv2[1], fv[2] + fv2[2], fv[3] + fv2[3]}
}

// Minus returns a new FourVector fv - fv2.
func (fv *FourVector) Minus(fv2 *FourVector) *FourVector {
	return &FourVector{fv[0] - fv2[0], fv[1] - fv2[1], fv[2] - fv2[2], fv[3] - fv2[3]}
}
