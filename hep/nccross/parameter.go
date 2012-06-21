package nccross

import (
	"fmt"
	"physics/hep/lhe"
	"physics/hep/pdg"
	"physics/math/linalg"
)

// Parameter contains all input parameter needed for calculating
// the cross section of pp -> chi^0 chi^+
type Parameter struct {
	N    *linalg.Matrix4 // Matrix for diagonalizing the neutralino mass matrix via N^T.M.N
	U    *linalg.Matrix2 // chargino mixing matrix
	V    *linalg.Matrix2 // chargino mixing matrix
	M_n  [4]float64      // Neutralino masses
	M_c  [2]float64      // Chargino masses
	M_su float64         // ~u_L mass
	M_sd float64         // ~d_L mass
	M_ss float64         // ~s_L mass
	M_sc float64         // ~c_L mass
}

// NewParameterFromLheFile reads the parameters from an input file at path.
func NewParameterFromLheFile(path string) (*Parameter, error) {
	lfile := lhe.NewFile()
	lfile.AddBlockCmd("mass", lhe.ReadList)
	lfile.AddBlockCmd("nmix", lhe.ReadMatrix4)
	lfile.AddBlockCmd("umix", lhe.ReadMatrix2)
	lfile.AddBlockCmd("vmix", lhe.ReadMatrix2)
	data, err := lfile.ReadFromFile(path)
	if err != nil {
		return nil, err
	}

	tmp, ok := data.Blocks["mass"]
	if ok != true {
		return nil, fmt.Errorf("no mass block in file: %s", path)
	}
	masses := tmp.(map[int]float64)

	N := data.Blocks["nmix"].(*linalg.Matrix4)
	U := data.Blocks["umix"].(*linalg.Matrix2)
	V := data.Blocks["vmix"].(*linalg.Matrix2)

	return &Parameter{
		N:    N,
		U:    U,
		V:    V,
		M_n:  [4]float64{masses[pdg.Neutralino1], masses[pdg.Neutralino2], masses[pdg.Neutralino3], masses[pdg.Neutralino4]},
		M_c:  [2]float64{masses[pdg.Chargino1], masses[pdg.Chargino2]},
		M_su: masses[pdg.SUQuarkL],
		M_sd: masses[pdg.SDQuarkL],
		M_ss: masses[pdg.SSQuarkL],
		M_sc: masses[pdg.SCQuarkL],
	}, nil
}
