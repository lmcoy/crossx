
GOROOT=$(shell go env GOROOT)
GOARCH=$(shell go env GOARCH)
GOOS=$(shell go env GOOS)
GOCHAR=$(shell go env GOCHAR)

GC=$(GOCHAR)g
CGO=$(GOCHAR)c
CPP=g++

.PHONY: lib go clean all

all: lib go

lib: mt2_bisect.so

go: mt2_bisect.go


mt2_bisect.o: mt2_bisect.h mt2_bisect.cpp
	$(CPP) -c -fpic mt2_bisect.cpp


mt2_bisect_wrap.o: mt2_bisect_wrap.cxx mt2_bisect.h
	$(CPP) -c -fpic mt2_bisect_wrap.cxx

mt2_bisect.go mt2_bisect_wrap.cxx mt2_bisect_gc.c: mt2_bisect.swigcxx mt2_bisect.h
	swig -go -c++ mt2_bisect.swigcxx
	go fmt mt2_bisect.go

mt2_bisect.so: mt2_bisect_wrap.o mt2_bisect.o
	$(CPP) -shared mt2_bisect_wrap.o mt2_bisect.o -o mt2_bisect.so

#mt2_bisect.$(GOCHAR): mt2_bisect.go
#	go tool $(GC) mt2_bisect.go

#mt2_bisect_gc.$(GOCHAR): mt2_bisect_gc.c
#	go tool $(CGO) -I ${GOROOT}/pkg/${GOOS}_${GOARCH} mt2_bisect_gc.c

#mt2.a: mt2_bisect_gc.$(GOCHAR) mt2_bisect.$(GOCHAR)
#	go tool pack grc mt2.a mt2_bisect_gc.$(GOCHAR) mt2_bisect.$(GOCHAR)

clean:
	rm -f mt2_bisect.o \
	mt2_bisect_wrap.o \
	mt2_bisect.so \
	mt2_bisect.$(GOCHAR) \
	mt2_bisect_gc.$(GOCHAR) \
	mt2_bisect.go \
	mt2_bisect_wrap.cxx \
	mt2_bisect_gc.c

