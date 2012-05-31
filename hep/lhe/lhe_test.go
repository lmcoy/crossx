package lhe

import (
	"physics/math/linalg"
	"testing"
	"fmt"
)

func TestLHE(t *testing.T) {
	lhe := NewFile()
	lhe.AddBlockCmd("mass", ReadList)
	lhe.AddBlockCmd("minpar", ReadList)
	lhe.AddBlockCmd("nmix", ReadMatrix4)
	data, err := lhe.ReadFromFile("testdata/test.lhe")
	if err != nil {
		t.Fatalf("unexpected error while reading les houces file: %s\n", err)
		return
	}

	tmp, ok := data.Blocks["mass"]
	if ok != true {
		t.Fatalf("Block mass not read!")
	}
	MASS := tmp.(map[int]float64)
	var mass5 float64
	mass5, ok = MASS[5]
	if ok != true {
		t.Fatalf("no mass for particle 5 found!")
	}
	emass5 := 4.88991651E+00 // expected mass
	if mass5 != emass5 {
		t.Fatalf("wrong mass for particle 5: got %e, expected %e", mass5, emass5)
	}

	tmp, ok = data.Blocks["nmix"]
	if ok != true {
		t.Fatalf("Block nmix not read!")
	}
	nmix := tmp.(*linalg.Matrix4)
	eN11 := 9.92797628E-01
	if nmix.At(0, 0) != eN11 {
		t.Fatalf("wrong N11 in nmix: got %e, expected %e", nmix.At(0, 0), eN11)
	}
	eN34 := 7.08979412E-01
	if nmix.At(2, 3) != eN34 {
		t.Fatalf("wrong N11 in nmix: got %e, expected %e", nmix.At(2, 3), eN11)
	}
}

func ExampleFile() {
	lhe := NewFile()
	lhe.AddBlockCmd("mass", ReadList)
	lhe.AddBlockCmd("minpar", ReadList)
	lhe.AddBlockCmd("nmix", ReadMatrix4)
	data, err := lhe.ReadFromFile("testdata/test.lhe")
	if err != nil {
		return
	}

	tmp, ok := data.Blocks["mass"]
	if ok != true {
		return
	}
	mass := tmp.(map[int]float64)
	var mass5 float64
	mass5, ok = mass[5]
	if ok != true {
		return
	}
	fmt.Printf( "mass for particle 5: %f\n", mass5 )
}