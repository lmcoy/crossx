package lhef

import (
	"math"
	"os"
	"physics/hep/kinematics"
	"physics/hep/pdg"
	"testing"
)

var preObjs = []*Object{
	&Object{
		Typ:           -1,
		State:         -1,
		Mother:        [2]int64{0, 0},
		Color:         [2]int64{0, 501},
		FourVector:    &kinematics.FourVector{0: 399.19743011, 1: 0, 2: 0, 3: 399.19743011},
		InvariantMass: 0,
		LifeTime:      0,
		Spin:          1,
	},
	&Object{
		Typ:           2,
		State:         -1,
		Mother:        [2]int64{0, 0},
		Color:         [2]int64{501, 0},
		FourVector:    &kinematics.FourVector{0: 3.9435316792, 1: 0, 2: 0, 3: -3.9435316792},
		InvariantMass: 0,
		LifeTime:      0,
		Spin:          -1,
	},
	&Object{
		Typ:           24,
		State:         2,
		Mother:        [2]int64{1, 2},
		Color:         [2]int64{0, 0},
		FourVector:    &kinematics.FourVector{0: 403.14096179, 1: 0, 2: 0, 3: 395.25389843},
		InvariantMass: 79.35358119,
		LifeTime:      0,
		Spin:          0,
	},
	&Object{
		Typ:           -11,
		State:         1,
		Mother:        [2]int64{3, 3},
		Color:         [2]int64{0, 0},
		FourVector:    &kinematics.FourVector{0: 318.99174739, 1: -30.323238127, 2: 9.9501563813, 3: 317.3912893},
		InvariantMass: 0,
		LifeTime:      0,
		Spin:          1,
	},
	&Object{
		Typ:           12,
		State:         1,
		Mother:        [2]int64{3, 3},
		Color:         [2]int64{0, 0},
		FourVector:    &kinematics.FourVector{0: 84.149214393, 1: 30.323238127, 2: -9.9501563813, 3: 77.862609129},
		InvariantMass: 0,
		LifeTime:      0,
		Spin:          -1,
	},
}

var preEvent = &Event{
	ID:          1,
	EventWeight: 49.226,
	Scale:       80.4,
	AlphaQED:    0.007546772,
	AlphaQCD:    0.129783,
	Objects:     preObjs,
}

// search checks whether f is in s.
func search(f int, s []int) bool {
	for _, i := range s {
		if i == f {
			return true
		}
	}
	return false
}

func TestParticleInState(t *testing.T) {
	final := preEvent.ParticlesInState(1)
	initial := preEvent.ParticlesInState(-1)
	intermediate := preEvent.ParticlesInState(2)
	if len(final) != 2 {
		t.Errorf("Expected 2 particles in final state. %d particles found", len(final))
	}
	if len(initial) != 2 {
		t.Errorf("Expected 2 particles in initial state. %d particles found", len(initial))
	}
	if len(intermediate) != 1 {
		t.Errorf("Expected 1 particles in intermediate state. %d particles found", len(intermediate))
	}
	// Can't go further because all subsequent tests assumes the above length of the slices.
	if t.Failed() {
		t.FailNow()
	}
	// check if particles are in wrong state
	if search(0, initial) == false {
		t.Errorf("index 0 is a initial state but not found as initial.")
	}
	if search(1, initial) == false {
		t.Errorf("index 1 is a initial state but not found as initial.")
	}
	if search(2, intermediate) == false {
		t.Errorf("index 1 is a intermediate state but not found as intermediate.")
	}
	if search(3, final) == false {
		t.Errorf("index 1 is a final state but not found as final.")
	}
	if search(4, final) == false {
		t.Errorf("index 1 is a final state but not found as final.")
	}
}

func TestNumberOfParticle(t *testing.T) {
	if preEvent.NumberOfParticle(pdg.Wplus, 2) != 1 {
		t.Errorf("There should be one W+ in intermediate state, but found %d W+.", preEvent.NumberOfParticle(pdg.Wplus, 2))
	}
	if preEvent.NumberOfParticle(-pdg.Electron, 1) != 1 {
		t.Errorf("There should be one e+ in final state, but found %d e+.", preEvent.NumberOfParticle(pdg.Electron, 1))
	}
	if preEvent.NumberOfParticle(pdg.UQuark, -1) != 1 {
		t.Errorf("There should be one e+ in initial state, but found %d e+.", preEvent.NumberOfParticle(pdg.UQuark, -1))
	}
	if preEvent.NumberOfParticle(-pdg.Muon, 1) != 0 {
		t.Errorf("There should be no mu+ in final state, but found %d mu+.", preEvent.NumberOfParticle(pdg.Muon, 1))
	}
}

func TestRead(t *testing.T) {
	file, err := os.Open("testdata/w+_production_lhc_0.lhe")
	if err != nil {
		t.Fatalf("could not open input file: %s", err)
	}
	defer file.Close()

	init, events, e := Read(file)
	if e != nil {
		t.Fatalf("error while reading lhe file: %s", e)
	}

	// check the content
	if init.BeamEnergy[0] != 3500.0 {
		t.Errorf("wrong beam energy 1:\nexpected: %8.3f\ngot:      %8.3f", 3500.0, init.BeamEnergy[0])
	}
	if init.BeamEnergy[1] != 3500.0 {
		t.Errorf("wrong beam energy 2:\nexpected: %8.3f\ngot:      %8.3f", 3500.0, init.BeamEnergy[1])
	}

	for i, event := range events {
		if len(event.Objects) != 5 {
			t.Errorf("event %d: event must consist of 5 particles but this event consist of %d particles.", i, len(event.Objects))
		}
		if event.NumberOfParticle(pdg.Wplus, 2) != 1 {
			t.Errorf("event %d: expected one W in intermediate mode for pp -> e nu. Found %d W's.", i, event.NumberOfParticle(pdg.Wplus, 2))
		}
		initial_states := event.ParticlesInState(-1)
		if len(initial_states) != 2 {
			t.Errorf("event %d: expected two particles in inital state. Found %d.", i, len(initial_states))
		}
		p1 := event.Objects[initial_states[0]].FourVector
		p2 := event.Objects[initial_states[1]].FourVector
		p_init := p1.Plus(p2)
		sqrts := math.Sqrt(p_init.Dot(p_init))
		if sqrts > 7000.0 {
			t.Errorf("event %d: inital states have too much energy, i.e. sqrt(s) = %8.3f > 7 TeV (collider sqrts(s))", i, sqrts)
		}
	}
}
