# Python Speed Benchmarks


This repository contains code used for benchmarking different methods
of improving code performance.

The computation to speed up is a simple euclidean distance formula.

I have tried the following methods:

* numba
* numpy
* scipy
* cython
* pythran
* fortran with f2py
* plain C with ctypes / cffi

## Instructions


Run this command to build binary modules:
	$ ./build-all.sh

Now we can run the benchmarks:

	$ ./main.py 
	Method               Time A [s]  Baseline A [x]      Time B [s]  Baseline B [x]
	python                     5.49            1.00            2.57            1.00
	pythran                    0.39           14.01            0.06           40.26
	numba                      0.76            7.23            0.07           38.63
	numpy                      2.55            2.15            0.11           22.74
	scipy                      2.70            2.03            0.07           37.68
	cython                     0.56            9.81            0.07           39.10
	Fortran                    0.39           14.15            0.06           40.27
	Ctypes                     2.27            2.42            0.07           39.26
	Cffi                       0.97            5.67            0.06           40.37

## Some Remarks

All in all, pythran gives us the best bang for the buck. I was very impressed. The resulting code speed ups are massive with virtually zero porting effort.

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
