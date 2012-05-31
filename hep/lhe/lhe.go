// The package lhe provides a reader for les houches files in particle physics.
package lhe

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"physics/math/linalg"
	"strconv"
	"strings"
)

// Block represents a block in a les houches file.
type Block interface{}

// Data contains all data which is read from a les houches file, e.g. blocks.
type Data struct {
	Blocks map[string]Block
}

type matrixElement struct {
	row    int
	column int
	value  float64
}

type ReadDataFn func(*File) (interface{}, error)

// File reads a les houches file from disk.
type File struct {
	currentLine int
	lines       []string
	block_cmds  map[string]ReadDataFn
	blocks      map[string]Block
}

// NewFile creates a new File.
func NewFile() *File {
	return &File{
		block_cmds: make(map[string]ReadDataFn),
		blocks:     make(map[string]Block),
	}
}

// AddBlockCmd specifies a function which is called for every line in a block name.
func (lhe *File) AddBlockCmd(name string, datafn ReadDataFn) {
	lhe.block_cmds[name] = datafn
}

// readLheFile reads the file at path line by line and stores its content in lhe for reading with readLine.
func (lhe *File) readLheFile(path string) (err error) {
	var (
		file   *os.File
		part   []byte
		prefix bool
	)
	lhe.lines = make([]string, 100)
	if file, err = os.Open(path); err != nil {
		return
	}
	defer file.Close()
	reader := bufio.NewReader(file)
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
			lhe.lines = append(lhe.lines, strings.ToLower(string(b)))
			buffer.Reset()
		}
	}
	if err == io.EOF {
		err = nil
	}
	return
}

// readLine returns the next not empty line
func (lhe *File) readLine() string {
	for ; lhe.currentLine < len(lhe.lines); lhe.currentLine++ {
		line := lhe.lines[lhe.currentLine]
		if strings.TrimSpace(line) != "" {
			lhe.currentLine++
			return line
		}
	}
	return "EMPTY"
}

// unreadLine set the currentLine to the previous not empty line.
func (lhe *File) unreadLine() bool {
	for ; lhe.currentLine > 0 && lhe.currentLine < len(lhe.lines); lhe.currentLine-- {
		line := lhe.lines[lhe.currentLine-1]
		if strings.TrimSpace(line) != "" {
			lhe.currentLine -= 1
			return true
		}
	}
	return false
}

func readMatrixElement(line string) (melem matrixElement, err error) {
	tokens := strings.Fields(line)
	if len(tokens) != 3 {
		return melem, fmt.Errorf("expected format for a matrix element \"row column value\".")
	}
	var row, column int64
	var value float64
	if row, err = strconv.ParseInt(tokens[0], 10, 32); err != nil {
		return melem, fmt.Errorf("unable to parse row number: %s", err)
	}
	if column, err = strconv.ParseInt(tokens[1], 10, 32); err != nil {
		return melem, fmt.Errorf("unable to parse column number: %s", err)
	}
	if value, err = strconv.ParseFloat(tokens[2], 64); err != nil {
		return melem, fmt.Errorf("unable to parse value: %s", err)
	}
	melem.row = int(row) - 1
	melem.column = int(column) - 1
	melem.value = value
	return
}

func ReadMatrix4(lhe *File) (interface{}, error) {
	matrix := linalg.NewMatrix4()
	for {
		line := lhe.readLine()
		if line[0] != ' ' {
			lhe.unreadLine()
			break
		}

		melem, err := readMatrixElement(line)
		if err != nil {
			return nil, err
		}
		matrix.Set(melem.row, melem.column, melem.value)
	}
	return matrix, nil
}

// readListElement returns from a line formated like "id(int)   value(float64)" both values.
func readListElement(line string) (id int, value float64, err error) {
	tokens := strings.Fields(line)
	if len(tokens) != 2 {
		return 0, 0.0, fmt.Errorf("expected format for a list element \"id value\".")
	}
	var tid int64
	if tid, err = strconv.ParseInt(tokens[0], 10, 32); err != nil {
		return 0, 0.0, fmt.Errorf("unable to parse id number: %s", err)
	}
	if value, err = strconv.ParseFloat(tokens[1], 64); err != nil {
		return int(tid), 0.0, fmt.Errorf("unable to parse value: %s", err)
	}
	return int(tid), value, nil
}

// ReadList reads block data with format "int  float64" and returns a map[int]float64 with the values.
func ReadList(lhe *File) (interface{}, error) {
	list := make(map[int]float64)
	for {
		line := lhe.readLine()
		if line[0] != ' ' {
			lhe.unreadLine()
			break
		}

		id, value, err := readListElement(line)
		if err != nil {
			return nil, err
		}
		list[id] = value
	}
	return list, nil
}

// skipData skips all data lines.
func skipData(lhe *File) (interface{}, error) {
	for {
		line := lhe.readLine()
		if line[0] != ' ' {
			lhe.unreadLine()
			break
		}
	}
	return nil, nil
}

// readBlock reads the data of block named para[0] if a Cmd was added with AddBlockCmd for this name.
// Otherwise it skips all data lines in the block.
func (lhe *File) readBlock(para []string) error {
	var err error
	var data interface{}

	datafn, ok := lhe.block_cmds[para[0]]
	if ok == true {
		data, err = datafn(lhe)
	} else {
		data, err = skipData(lhe)
	}
	if err != nil {
		return err
	}
	if data != nil {
		lhe.blocks[para[0]] = data
	}
	return nil
}

// parse parses the data in lhe.lines.
func (lhe *File) parse() (err error) {
	for {
		line := lhe.readLine()
		if line == "EMPTY" { // NO MORE LINES
			break
		}
		if line[0] == 0 {
			continue
		}
		fields := strings.Fields(line)
		if len(fields) == 0 {
			return fmt.Errorf("empty line")
		}
		switch {
		case fields[0] == "block":
			err = lhe.readBlock(fields[1:])
		default:
			_, err = skipData(lhe)
		}
		if err != nil {
			return err
		}
	}
	return
}

// ReadFromFile reads the les houches file from path.
//
// It returns all data read by BlockCmds (which are provided by AddBlockCmd).
func (lhe *File) ReadFromFile(path string) (*Data, error) {
	err := lhe.readLheFile(path)
	if err != nil {
		return nil, err
	}
	err = lhe.parse()
	if err != nil {
		return nil, err
	}
	return &Data{
		Blocks: lhe.blocks,
	}, nil
}
