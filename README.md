# Python Speed Benchmarks

This repository contains source code used for benchmarking different methods
of improving performance of numerical computations in Python.

The calculation to speed up is a simple euclidean distance formula.

I have tried the following methods:

* numba
* numpy
* scipy
* cython
* pythran
* fortran with f2py
* plain C with ctypes, cffi and SWIG

## Instructions

Run this command to build binary modules:

	$ ./build-all.sh

Now we can run the benchmarks:

	$ ./main.py 
	Method              Med. A [ms]   Speedup A [x]     Med. B [ms]   Speedup B [x]
	python                   0.0534            1.00        106.6365            1.00
	pythran                  0.0041           13.18          2.0952           50.90
	numba                    0.0045           11.79          2.2156           48.13
	numpy                    0.0257            2.07          4.0476           26.35
	scipy                    0.0265            2.02          2.9585           36.04
	cython                   0.0057            9.33          2.1977           48.52
	Fortran                  0.0041           13.18          2.1245           50.19
	Ctypes                   0.0217            2.46          2.1193           50.32
	Cffi                     0.0098            5.46          2.1205           50.29
	SWIG                     0.0045           11.79          3.1922           33.41

## Remarks

All in all, pythran gives us the best bang for the buck. I was very impressed.
The resulting code speedups are massive with virtually zero porting effort.

Ctypes seems to incur a lot of overhead for calling functions.

f2py does excellent job.

## Links

Pythran
https://pythran.readthedocs.io/en/latest/

Numba
https://numba.pydata.org/

Cython
https://cython.org/

f2py
https://numpy.org/doc/stable/f2py/

Numpy
https://numpy.org/

Scipy
https://scipy.org/

Ctypes
https://docs.python.org/3/library/ctypes.html

Cffi
https://cffi.readthedocs.io/en/latest/

SWIG
http://www.swig.org/
