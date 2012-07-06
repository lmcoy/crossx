package lhco

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

type Type int

const (
	Photon Type = iota
	Electron
	Muon
	Tau
	Jet
	MissingTransverseEnergy
)

const (
	photonString            = "photon"
	electronString          = "electron"
	muonString              = "muon"
	tauString               = "tau"
	jetString               = "jet"
	missingTransverseString = "missing transverse energy"
)

func (t Type) String() string {
	switch t {
	case Photon:
		return photonString
	case Electron:
		return electronString
	case Muon:
		return muonString
	case Tau:
		return tauString
	case Jet:
		return jetString
	case MissingTransverseEnergy:
		return missingTransverseString
	}
	return "unkown object"
}

// Object represents an object seen by the detector
type Object struct {
	// type of the object
	Typ Type
	// Pseudorapidity, azimuthal angle, transverse momentum
	Eta           float64
	Phi           float64
	PT            float64
	InvariantMass float64
	// number of tracks (for leptons this number is multiplied with the charge)
	NumberOfTracks float64
	// 1 or 2 for a jet that has been "tagged" as containing a b-quark otherwise it is 0.
	Btag float64
	// hadronic versus electromagnetic energy deposited 
	// in the calorimeter cells associated with the object.
	HadVsEmEnergy float64
	// For future use: should always be 0.0 at the moment
	Dummy1 float64
	Dummy2 float64
}

// Event is an event in the detector
type Event struct {
	// event number
	N              int
	TriggeringInfo int
	// objects in the event
	Objects []Object
}

func (e *Event) String() string {
	result := "{"
	for i, o := range e.Objects {
		result += fmt.Sprintf("%s", o.Typ.String())
		if i < len(e.Objects)-1 {
			result += ", "
		}
	}
	result += "}"
	return result
}

// NumberOfJets returns the number of jets in the event.
func (e *Event) NumberOfJets() int {
	jets := 0
	for _, o := range e.Objects {
		if o.Typ == Jet {
			jets += 1
		}
	}
	return jets
}

// NumberOfPhotons returns the number of photons in the event.
func (e *Event) NumberOfPhotons() int {
	photons := 0
	for _, o := range e.Objects {
		if o.Typ == Photon {
			photons += 1
		}
	}
	return photons
}

// NumberOfMuons returns the number of muons in the event.
func (e *Event) NumberOfMuons() (plus, minus int) {
	for _, o := range e.Objects {
		if o.Typ == Muon {
			switch {
			case o.NumberOfTracks < 0:
				minus += 1
			case o.NumberOfTracks > 0:
				plus += 1
			}
		}
	}
	return
}

// NumberOfElectrons returns the number of electrons in the event.
func (e *Event) NumberOfElectrons() (plus, minus int) {
	for _, o := range e.Objects {
		if o.Typ == Electron {
			switch {
			case o.NumberOfTracks < 0:
				minus += 1
			case o.NumberOfTracks > 0:
				plus += 1
			}
		}
	}
	return
}

func (e *Event) NumberOfTaus() (plus, minus int) {
	for _, o := range e.Objects {
		if o.Typ == Tau {
			switch {
			case o.NumberOfTracks < 0:
				minus += 1
			case o.NumberOfTracks > 0:
				plus += 1
			}
		}
	}
	return
}

// NumberOfObjects returns the amount of each particle/object in the event.
//
//     0: Number of photons
//     1: Number of electrons
//     2: Number of muons
//     3: Number of taus
//     4: Number of jets
func (e *Event) NumberOfObjects() (count []int) {
	count = make([]int, 5)
	for _, o := range e.Objects {
		switch o.Typ {
		case Photon:
			count[0] += 1
		case Electron:
			count[1] += 1
		case Muon:
			count[2] += 1
		case Tau:
			count[3] += 1
		case Jet:
			count[4] += 1
		}
	}
	return
}

// readLines reads all lines from an io.Reader.
//
// It removes all comments beginning with #.
func readLines(r io.Reader) (lines []string, err error) {
	var (
		part   []byte
		prefix bool
	)
	lines = make([]string, 0, 100)
	reader := bufio.NewReader(r)
	buffer := bytes.NewBuffer(make([]byte, 1024))
	for {
		if part, prefix, err = reader.ReadLine(); err != nil {
			break
		}
		buffer.Write(part)
		if !prefix {
			// remove comments
			b := buffer.Bytes()
			if index := bytes.IndexAny(b, "#"); index >= 0 {
				b = b[0:index]
			}
			lines = append(lines, strings.ToLower(string(b)))
			buffer.Reset()
		}
	}
	if err == io.EOF {
		err = nil
	}
	return
}

// ReadFromFile reads the events from the file at path.
func ReadFromFile(path string) (events []*Event, err error) {
	var (
		file *os.File
	)
	if file, err = os.Open(path); err != nil {
		return make([]*Event, 0), fmt.Errorf("error while opening \"%s\": %s", path, err.Error())
	}
	defer file.Close()

	return Read(file)
}

// Read reads the events form an io.Reader.
func Read(r io.Reader) (events []*Event, err error) {
	var (
		lines        []string
		currentEvent *Event
		e            error
	)

	lines, err = readLines(r)
	if err != nil {
		return make([]*Event, 0), err
	}
	events = make([]*Event, 0, 1000)

	for linenb, line := range lines {
		var (
			nb, N, tinfo int64
		)
		fields := strings.Fields(line)
		if len(fields) <= 1 {
			// empty line
			continue
		}
		nb, e = strconv.ParseInt(fields[0], 10, 64)
		if e != nil {
			return events, fmt.Errorf("line %d column 1: expected number: %s\n", linenb+1, e.Error())
		}

		switch {
		case nb == 0:
			if currentEvent != nil {
				events = append(events, currentEvent)
			}
			if len(fields) != 3 {
				return events, fmt.Errorf("line %d: too many columns in first line of an event.", linenb+1)
			}
			N, e = strconv.ParseInt(fields[1], 10, 32)
			if e != nil {
				return events, fmt.Errorf("line %d column 2: expected event number: %s\n", linenb+1, e.Error())
			}
			tinfo, e = strconv.ParseInt(fields[1], 10, 32)
			if e != nil {
				return events, fmt.Errorf("line %d column 3: expected TriggeringInfo (number): %s\n", linenb+1, e.Error())
			}
			currentEvent = &Event{
				N:              int(N),
				TriggeringInfo: int(tinfo),
				Objects:        make([]Object, 0, 2),
			}
		case nb > 0:
			if currentEvent == nil {
				return events, fmt.Errorf("line %d: missing event definition line.", linenb+1)
			}
			if len(fields) != 11 {
				return events, fmt.Errorf("line %d: too many or too few columns for an object.", linenb+1)
			}
			var typ int64
			typ, e = strconv.ParseInt(fields[1], 10, 64)
			if e != nil {
				return events, fmt.Errorf("line %d column 2: expected pseudorapidity (float): %s", linenb+1, e.Error())
			}
			var values []float64
			values, e = convertToFloat64(fields[2:])
			if e != nil {
				return events, fmt.Errorf("line %d: %s", linenb+1, e.Error())
			}
			object := Object{
				Typ:            Type(typ),
				Eta:            values[0],
				Phi:            values[1],
				PT:             values[2],
				InvariantMass:  values[3],
				NumberOfTracks: values[4],
				Btag:           values[5],
				HadVsEmEnergy:  values[6],
				Dummy1:         values[7],
				Dummy2:         values[8],
			}
			currentEvent.Objects = append(currentEvent.Objects, object)
		}
	}
	return
}

// convertFloat64 converts all strings in the slice fields to float64.
func convertToFloat64(fields []string) (values []float64, err error) {
	values = make([]float64, len(fields))
	for i, field := range fields {
		value := 0.0
		value, err = strconv.ParseFloat(field, 64)
		if err != nil {
			return values, fmt.Errorf("could not convert \"%s\" to float64: %s", field, err.Error())
		}
		values[i] = value
	}
	return
}
