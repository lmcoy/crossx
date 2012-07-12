// The package pdg contains particle data from http://pdg.lbl.gov/
package pdg

type Particle int

const (
	// PDG codes for particles
	// anti particles are denoted with a minus, e.g. anti d quark: -DQuark
	// Quarks
	DQuark      Particle = 1
	UQuark      Particle = 2
	SQuark      Particle = 3
	CQuark      Particle = 4
	BQuark      Particle = 5
	TQuark      Particle = 6
	BQuarkPrime Particle = 7
	TQuarkPrime Particle = 8
	// Leptons
	Electron         Particle = 11
	ElectronNeutrino Particle = 12
	Muon             Particle = 13
	MuonNeutrino     Particle = 14
	Tau              Particle = 15
	TauNeutrino      Particle = 16
	TauPrime         Particle = 17
	TauPrimeNeutrino Particle = 18
	// Gauge
	Gluon  Particle = 21
	Photon Particle = 22
	Z      Particle = 23
	Wplus  Particle = 24
	// Higgs
	Higgs       Particle = 25
	ZPrime      Particle = 32
	ZPrimePrime Particle = 33
	WPrime      Particle = 34
	H0          Particle = 35
	A0          Particle = 36
	HPlus       Particle = 37
	// SUSY
	SDQuarkL           Particle = 1000001
	SUQuarkL           Particle = 1000002
	SSQuarkL           Particle = 1000003
	SCQuarkL           Particle = 1000004
	SElectronL         Particle = 1000011
	SElectronNeutrinoL Particle = 1000012
	SMuonL             Particle = 1000013
	SMuonNeutrinoL     Particle = 1000014
	SDQuarkR           Particle = 2000001
	SUQuarkR           Particle = 2000002
	SSQuarkR           Particle = 2000003
	SCQuarkR           Particle = 2000004
	SElectronR         Particle = 2000011
	SMuonR             Particle = 2000013
	Neutralino1        Particle = 1000022
	Neutralino2        Particle = 1000023
	Neutralino3        Particle = 1000025
	Neutralino4        Particle = 1000035
	Chargino1          Particle = 1000024
	Chargino2          Particle = 1000037
	// Light I=1 Mesons
	Pi0    Particle = 111
	PiPlus Particle = 211
	// Light I=0 Mesons
	Eta      Particle = 221
	EtaPrime Particle = 331
	// Strange Mesons
	Kaon     Particle = 311
	KaonPlus Particle = 321
	// cc~ Mesons
	JPsi Particle = 443
	// Light Baryons
	Proton        Particle = 2212
	Neutron       Particle = 2112
	DeltaPlusPlus Particle = 2224
	DeltaPlus     Particle = 2114
	Delta0        Particle = 2114
	DeltaMinus    Particle = 1114
)

// global variables which should be accessed by Jet() ... only. 
// Important: This variables should never be changed!
var jet = [...]Particle{Gluon, UQuark, -UQuark, DQuark, -DQuark, SQuark, -SQuark, CQuark, -CQuark}
var neutrino = [...]Particle{ElectronNeutrino, MuonNeutrino, TauNeutrino}
var antiNeutrino = [...]Particle{-ElectronNeutrino, -MuonNeutrino, -TauNeutrino}

// Jet returns a slice with all particles which leads to jets, i.e. Gluon, U, D, C, S and antiquarks
func Jet() (j []Particle) {
	j = make([]Particle, len(jet))
	copy(j, jet[0:])
	return
}

// Neutrino returns a slice with all neutrinos.
func Neutrino(n []Particle) {
	n = make([]Particle, len(neutrino))
	copy(n, neutrino[0:])
	return
}

// AntiNeutrino returns a slice with all anti-neutrinos.
func AntiNeutrino(n []Particle) {
	n = make([]Particle, len(antiNeutrino))
	copy(n, antiNeutrino[0:])
	return
}
