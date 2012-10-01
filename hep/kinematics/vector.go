package kinematics

import (
	"math"
	"physics/math/linalg"
)

func DeltaPhi(v1, v2 *linalg.Vector3D) float64 {
	phi1 := math.Atan2(v1[1], v1[0])
	phi2 := math.Atan2(v2[1], v2[0])

	dPhi := phi1 - phi2

	for dPhi >= math.Pi {
		dPhi -= 2.0 * math.Pi
	}
	for dPhi < -math.Pi {
		dPhi += 2.0 * math.Pi
	}
	return dPhi
}

func pseudoRapidity(v *linalg.Vector3D) float64 {
	tmp := math.Sqrt(v[0]*v[0] + v[1]*v[1])
	theta := math.Atan2(tmp, v[2])
	return -math.Log(math.Tan(theta / 2.0))
}

func DeltaR(v1, v2 *linalg.Vector3D) float64 {
	eta1 := pseudoRapidity(v1)
	eta2 := pseudoRapidity(v2)
	dEta := eta1 - eta2
	dPhi := DeltaPhi(v1, v2)
	return math.Sqrt(dEta*dEta + dPhi*dPhi)
}
