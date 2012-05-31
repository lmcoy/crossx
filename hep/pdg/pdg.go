// The package pdg contains particle data from http://pdg.lbl.gov/
package pdg

// PDG codes for particles
// anti particles are denoted with a minus, e.g. anti d quark: -DQuark
const (
	// Quarks
	DQuark = 1
	UQuark = 2
	SQuark = 3
	CQuark = 4
	BQuark = 5
	TQuark = 6
	// Leptons
	Electron         = 11
	ElectronNeutrino = 12
	Muon             = 13
	MuonNeutrino     = 14
	Tau              = 15
	TauNeutrino      = 16
	// Gauge
	Gluon  = 21
	Photon = 22
	Z      = 23
	Wplus  = 24
	// Higgs
	Higgs = 25
	//SUSY
	SDQuarkL           = 1000001
	SUQuarkL           = 1000002
	SSQuarkL           = 1000003
	SCQuarkL           = 1000004
	SElectronL         = 1000011
	SElectronNeutrinoL = 1000012
	SMuonL             = 1000013
	SMuonNeutrinoL     = 1000014
	SDQuarkR           = 2000001
	SUQuarkR           = 2000002
	SSQuarkR           = 2000003
	SCQuarkR           = 2000004
	SElectronR         = 2000011
	SMuonR             = 2000013
	Neutralino1        = 1000022
	Neutralino2        = 1000023
	Neutralino3        = 1000025
	Neutralino4        = 1000035
	Chargino1          = 1000024
	Chargino2          = 1000037
)
