1. Python Speed Benchmarks
====

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

2. Instructions
====

Run this command to build binary modules:
$ ./build-all.sh

Now we can run the benchmarks:

$ ./main.py 
Method               Time A [s]  Baseline A [x]      Time B [s]  Baseline B [x]
python                     5.19            1.00            4.99            1.00
pythran                    0.40           12.83            0.06           77.07
numba                      0.78            6.69            0.07           72.39
numpy                      2.62            1.98            0.11           45.80
scipy                      2.72            1.91            0.07           72.79
cython                     0.57            9.07            0.07           75.17
Fortran                    0.40           13.02            0.06           76.90
Ctypes                     2.18            2.37            0.06           76.91
Cffi                       0.96            5.42            0.06           77.67

3. Some Remarks
====

All in all, pythran gives us the best bang for the buck. I was very impressed.

The code speed-ups are massive with virually zero porting effort.

Ctypes seems to incur a lot of overhead for calling functions.

f2py does excellent job.

4. Links
====

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
