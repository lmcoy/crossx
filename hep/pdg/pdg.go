// The package pdg contains particle data from http://pdg.lbl.gov/
package pdg

const (
	// PDG codes for particles
	// anti particles are denoted with a minus, e.g. anti d quark: -DQuark
	// Quarks
	DQuark      = 1
	UQuark      = 2
	SQuark      = 3
	CQuark      = 4
	BQuark      = 5
	TQuark      = 6
	BQuarkPrime = 7
	TQuarkPrime = 8
	// Leptons
	Electron         = 11
	ElectronNeutrino = 12
	Muon             = 13
	MuonNeutrino     = 14
	Tau              = 15
	TauNeutrino      = 16
	TauPrime         = 17
	TauPrimeNeutrino = 18
	// Gauge
	Gluon  = 21
	Photon = 22
	Z      = 23
	Wplus  = 24
	// Higgs
	Higgs       = 25
	ZPrime      = 32
	ZPrimePrime = 33
	WPrime      = 34
	H0          = 35
	A0          = 36
	HPlus       = 37
	// SUSY
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
	// Light I=1 Mesons
	Pi0    = 111
	PiPlus = 211
	// Light I=0 Mesons
	Eta      = 221
	EtaPrime = 331
	// Strange Mesons
	Kaon     = 311
	KaonPlus = 321
	// cc~ Mesons
	JPsi = 443
	// Light Baryons
	Proton        = 2212
	Neutron       = 2112
	DeltaPlusPlus = 2224
	DeltaPlus     = 2114
	Delta0        = 2114
	DeltaMinus    = 1114
)
