
#all: pdf.a
all: libpdf.so

pdf.o: pdf.h pdf.cpp
	g++ -fPIC -O2 -o pdf.o -c pdf.cpp


libpdf.so: pdf.o
	gcc -shared -Wl,-soname,libpdf.so -o libpdf.so pdf.o -lc
#pdf.a: pdf.o
	#ar rcs libpdf.a pdf.o

