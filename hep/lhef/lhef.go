// The package lhef implements the les houches event file format.
//
// For a specification of the lhe file format see http://arXiv.org/abs/hep-ph/0609017v1
package lhef

import (
	"bytes"
	"encoding/xml"
	"fmt"
	"io"
	"physics/hep/kinematics"
	"physics/hep/pdg"
	"strconv"
	"strings"
)

const (
	InitialState      = -1
	FinalState        = 1
	IntermediateState = 2
)

// Object represents particles in an event.
type Object struct {
	// PDG monte carlo code of particle
	// name in format specification: IDUP
	Typ pdg.Particle
	// name in format specification: ISTUP
	State int64
	// name in format specification: MOTHUP
	Mother [2]int64
	// name in format specification: ICOLUP
	Color [2]int64
	// name in format specification: PUP
	FourVector *kinematics.FourVector
	// name in format specification: PUP
	InvariantMass float64
	// Proper lifetime
	// name in format specification: VTIMUP
	LifeTime float64
	// name in format specification: SPINUP
	Spin float64
}

// Event contains a <event>
type Event struct {
	// name in format specification: IDPRUP
	ID int64
	// name in format specification: XWGTUP
	EventWeight float64
	// name in format specification: SCALUP
	Scale float64
	// name in format specification: AQEDUP
	AlphaQED float64
	// name in format specification: AQCDUP
	AlphaQCD float64
	Objects  []*Object
}

// NumberOfParticle returns the number of particle with pdfcode and state.
func (e *Event) NumberOfParticle(pdgcode pdg.Particle, state int) (count int) {
	for _, obj := range e.Objects {
		if obj.State == int64(state) && obj.Typ == pdgcode {
			count += 1
		}
	}
	return
}

// FindParticle returns the indices of particles of type pdgcodes in a certain state.
func (e *Event) FindParticle(state int, pdgcodes ...pdg.Particle) (index []int) {
	index = make([]int, 0, 2*len(pdgcodes))
	for i, obj := range e.Objects {
		if obj.State == int64(state) {
			for _, pdg := range pdgcodes {
				if obj.Typ == pdg {
					index = append(index, i)
					break
				}
			}
		}
	}
	return
}

// ParticlesInState returns the indices of particles which are in a certain state.
func (e *Event) ParticlesInState(state int) (indices []int) {
	indices = make([]int, 0, len(e.Objects))
	for i, obj := range e.Objects {
		if obj.State == int64(state) {
			indices = append(indices, i)
		}
	}
	return
}

// Process contains information about a process which
// was used for event generation.
type Process struct {
	// name in format specification: LPRUP
	ID int64
	// name in format specification: XSECUP
	CrossSection float64
	// name in format specification: XERRUP
	CrossSectionError float64
	// name in format specification: XMAXUP
	Max float64
}

// Info contains informations of the initial states
// and processes from which the events are generated.
//
// Info contains all informations of <init>.
type Info struct {
	// name in format specification: IDBMUP
	BeamID [2]int64
	// name in format specification: EBMUP
	BeamEnergy [2]float64
	// name in format specification: PDFGUP
	PDFG [2]int64
	// name in format specification: PDFSUP
	PDFS [2]int64
	// name in format specification: IDWTUP
	WeightID  int64
	Processes []Process
}

// parseInit parses the content of <init> in a lhe file.
func parseInit(input []byte) (info *Info, err error) {
	lines := readLines(bytes.Trim(input, "\n\r"))
	if len(lines) < 2 {
		return nil, fmt.Errorf("init must contain at least two lines. %d", len(lines))
	}
	info = &Info{}
	fields := strings.Fields(lines[0])

	if len(fields) != 10 {
		return nil, fmt.Errorf("first line of <init> must consist of 10 values!")
	}
	// parse first line
	if info.BeamID[0], err = strconv.ParseInt(fields[0], 10, 32); err != nil {
		return nil, fmt.Errorf("could not read BeamID in column 1: %s", err)
	}
	if info.BeamID[1], err = strconv.ParseInt(fields[1], 10, 32); err != nil {
		return nil, fmt.Errorf("could not read BeamID in column 2: %s", err)
	}
	if info.BeamEnergy[0], err = strconv.ParseFloat(fields[2], 64); err != nil {
		return nil, fmt.Errorf("could not read beam energy in column 3: %s", err)
	}
	if info.BeamEnergy[1], err = strconv.ParseFloat(fields[3], 64); err != nil {
		return nil, fmt.Errorf("could not read beam energy in column 4: %s", err)
	}
	if info.PDFG[0], err = strconv.ParseInt(fields[4], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read PDFG in column 5: %s", err)
	}
	if info.PDFG[1], err = strconv.ParseInt(fields[5], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read PDFG in column 6: %s", err)
	}
	if info.PDFS[0], err = strconv.ParseInt(fields[6], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read PDFS in column 7: %s", err)
	}
	if info.PDFS[1], err = strconv.ParseInt(fields[7], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read PDFS in column 8: %s", err)
	}
	if info.WeightID, err = strconv.ParseInt(fields[8], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read WeightID in column 9: %s", err)
	}
	var numProcesses int64
	if numProcesses, err = strconv.ParseInt(fields[9], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read number of processes in colum 10: %s", err)
	}

	// check if infos in file are consistent.
	if numProcesses != int64(len(lines)-1) {
		return nil, fmt.Errorf("<init> says there are %d processes but only %d are available", numProcesses, len(lines)-1)
	}

	// parse the lines with processes
	for i, line := range lines[1:] {
		var p *Process
		if p, err = parseProcess(line); err != nil {
			return nil, fmt.Errorf("error while parsing process %d: %s", i+1, err)
		}
		info.Processes = append(info.Processes, *p)
	}

	return
}

// parseProcess parses a line with a process in <init>.
func parseProcess(line string) (p *Process, err error) {
	p = &Process{}
	fields := strings.Fields(line)
	if len(fields) != 4 {
		return nil, fmt.Errorf("wrong number of columns in process")
	}
	// Parse all all columns
	// format: crosssection  error  Max  ID
	if p.CrossSection, err = strconv.ParseFloat(fields[0], 64); err != nil {
		return nil, fmt.Errorf("could not read cross section: %s", err)
	}
	if p.CrossSectionError, err = strconv.ParseFloat(fields[1], 64); err != nil {
		return nil, fmt.Errorf("could not read cross section error: %s", err)
	}
	if p.Max, err = strconv.ParseFloat(fields[2], 64); err != nil {
		return nil, fmt.Errorf("could not read Max: %s", err)
	}
	if p.ID, err = strconv.ParseInt(fields[3], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read ID: %s", err)
	}
	return
}

// parseEvent parses the content of an <event>
func parseEvent(input []byte) (event *Event, err error) {
	lines := readLines(bytes.Trim(input, "\n\r"))
	if len(lines) < 2 {
		return nil, fmt.Errorf("<event> must contain at least two lines. %d", len(lines))
	}
	event = &Event{}
	fields := strings.Fields(lines[0])

	// parse 1st line
	var numberOfObjects int64
	if numberOfObjects, err = strconv.ParseInt(fields[0], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read number of particles in column 1: %s", err)
	}
	if numberOfObjects != int64(len(lines)-1) {
		return nil, fmt.Errorf("<event> says that there are %d objects but found %d objects.", numberOfObjects, len(lines))
	}
	if event.ID, err = strconv.ParseInt(fields[1], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read ID in column 2: %s", err)
	}
	if event.EventWeight, err = strconv.ParseFloat(fields[2], 64); err != nil {
		return nil, fmt.Errorf("could not read weight in column 3: %s", err)
	}
	if event.Scale, err = strconv.ParseFloat(fields[3], 64); err != nil {
		return nil, fmt.Errorf("could not read scale in column 4: %s", err)
	}
	if event.AlphaQED, err = strconv.ParseFloat(fields[4], 64); err != nil {
		return nil, fmt.Errorf("could not read alpha qed in column 5: %s", err)
	}
	if event.AlphaQCD, err = strconv.ParseFloat(fields[5], 64); err != nil {
		return nil, fmt.Errorf("could not read alpha qcd in column 6: %s", err)
	}

	// parse the lines with objects(particles)
	for i, line := range lines[1:] {
		var obj *Object
		if obj, err = parseObject(line); err != nil {
			return nil, fmt.Errorf("error while parsing object %d: %s", i+1, err)
		}
		event.Objects = append(event.Objects, obj)
	}
	return
}

// paresOject parses a line with a particle.
func parseObject(line string) (obj *Object, err error) {
	obj = &Object{}
	fields := strings.Fields(line)
	if len(fields) != 13 {
		return nil, fmt.Errorf("wrong number of columns for an object in an event: %d expected: %d.", len(fields), 13)
	}
	var pdgCode int64
	if pdgCode, err = strconv.ParseInt(fields[0], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read ID: %s", err)
	}
	obj.Typ = pdg.Particle(pdgCode)
	if obj.State, err = strconv.ParseInt(fields[1], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read state: %s", err)
	}
	if obj.Mother[0], err = strconv.ParseInt(fields[2], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read mother: %s", err)
	}
	if obj.Mother[1], err = strconv.ParseInt(fields[3], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read mother: %s", err)
	}
	if obj.Color[0], err = strconv.ParseInt(fields[4], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read color: %s", err)
	}
	if obj.Color[1], err = strconv.ParseInt(fields[5], 10, 64); err != nil {
		return nil, fmt.Errorf("could not read color: %s", err)
	}

	// parse four vector (PUP). 
	// 1st three columns contains momentm (px, py, pz)
	// 4th column contains p^0
	var fvector [4]float64
	if fvector[0], err = strconv.ParseFloat(fields[6], 64); err != nil {
		return nil, fmt.Errorf("could not read four vector component: %s", err)
	}
	if fvector[1], err = strconv.ParseFloat(fields[7], 64); err != nil {
		return nil, fmt.Errorf("could not read four vector component: %s", err)
	}
	if fvector[2], err = strconv.ParseFloat(fields[8], 64); err != nil {
		return nil, fmt.Errorf("could not read four vector component: %s", err)
	}
	if fvector[3], err = strconv.ParseFloat(fields[9], 64); err != nil {
		return nil, fmt.Errorf("could not read four vector component: %s", err)
	}

	obj.FourVector = kinematics.NewFourVector(fvector[3], fvector[0], fvector[1], fvector[2])

	// invariant mass (PUP(5))
	if obj.InvariantMass, err = strconv.ParseFloat(fields[10], 64); err != nil {
		return nil, fmt.Errorf("could not read invariant mass: %s", err)
	}

	if obj.LifeTime, err = strconv.ParseFloat(fields[11], 64); err != nil {
		return nil, fmt.Errorf("could not read life time: %s", err)
	}

	if obj.Spin, err = strconv.ParseFloat(fields[12], 64); err != nil {
		return nil, fmt.Errorf("could not read spin: %s", err)
	}

	return
}

// readLines splits input to multiple lines.
func readLines(input []byte) []string {
	return strings.SplitAfter(string(input), "\n")
}

// Read reads an lhe file from io.Reader.
//
// info contains the data of <init> and events the data
// of all <event> blocks.
func Read(r io.Reader) (info *Info, events []*Event, err error) {
	decoder := xml.NewDecoder(r)
	events = make([]*Event, 0, 10000)

	for {
		t, err := decoder.Token()
		if err != nil {
			if err == io.EOF {
				// EOF is not an error
				err = nil
			} else {
				return nil, nil, err
			}
		}
		// there are no more tokens
		if t == nil {
			break
		}

		switch se := t.(type) {
		case xml.StartElement:
			switch se.Name.Local {
			case "init": // parse <init>
				var e struct {
					Content []byte `xml:",chardata"`
				}
				decoder.DecodeElement(&e, &se)
				info, err = parseInit(e.Content)
				if err != nil {
					return nil, nil, err
				}
			case "event": // parse <event>
				var e struct {
					Content []byte `xml:",chardata"`
				}
				decoder.DecodeElement(&e, &se)
				var event *Event
				event, err = parseEvent(e.Content)
				if err != nil {
					return nil, nil, err
				}
				events = append(events, event)
			}
		}
	}
	return
}
