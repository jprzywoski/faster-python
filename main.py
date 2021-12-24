#!/usr/bin/env python3
"""
This is the main benchmark script used for timing different methods of
speeding python code up.

'dist' function is just a simple kernel implementing euclidean distance
formula using different methods.

The output of this script is a comparison table containing the average
execution times for different implementations.

The central tendency is reported as median value, just to avoid noisy readings.

"""
from time import time
import pyeuclid
import numpy as np
import npeuclid
import numbaeuclid
from scipy.spatial.distance import euclidean
import pthreuclid
import pyxeuclid
import forteuclid
import ceuclid
import cffieuclid
import cdist


#
# Those constants are used to execute two test cases:
# A. Calling our function many times with a relatively small amount of data
# and
# B. Calling our function relatively small amount of times with a large amount
# of data
#
# Notes
# Function calls in Python are expensive, hence the speedups will be different
# for each case.
# The numbers look weird - using odd numbers allows for trivial calculation of
# median values. Median is more resilient to outliers / noise than the
# arithmetic mean.
#
NCALLS_A = 100001
ARRAYSIZE_A = 51

NCALLS_B = 25
ARRAYSIZE_B = 100001

#
# Holds 2-tuples of this format: ("name", fn)
#
distfns = [
    ("pythran", pthreuclid.dist),
    ("numba", numbaeuclid.dist),
    ("numpy", npeuclid.dist),
    ("scipy", euclidean),
    ("cython", pyxeuclid.dist),
    ("Fortran", forteuclid.dist),
    ("Ctypes", ceuclid.dist),
    ("Cffi", cffieuclid.dist),
    ("SWIG", cdist.dist),
]


def benchmark(fn, niter, arrsize):
    """ Returns median execution time in ms. """
    times = []
    for _ in range(niter):
        start = time()        
        fn(np.random.rand(arrsize), np.random.rand(arrsize))
        times.append(time() - start)
    medidx = int(len(times) / 2)
    return 1000 * sorted(times)[medidx]


#
# Here we loop over our functions and calculate the execution times
# Pure python implementation is used as a baseline for other benchmarks.
#
baseline_a = benchmark(pyeuclid.dist, NCALLS_A, ARRAYSIZE_A)
baseline_b = benchmark(pyeuclid.dist, NCALLS_B, ARRAYSIZE_B)
NAME = 0
FN = 1
FMTSTR = "{0: <15}{1:16.4f}{2:16.2f}{3:16.4f}{4:16.2f}"
print("{0: <15}{1: >16}{2: >16}{3: >16}{4: >16}".format(
    "Method", "Med. A [ms]", "Speedup A [x]", "Med. B [ms]",
    "Speedup B [x]"))
print(FMTSTR.format("python", baseline_a, baseline_a /
                    baseline_a, baseline_b, baseline_b / baseline_b))
for distfn in distfns:
    name = distfn[NAME]
    euclidean = distfn[FN]

    #
    # Test case A
    #
    time_taken_a = benchmark(euclidean, NCALLS_A, ARRAYSIZE_A)

    #
    # Test case B
    #
    time_taken_b = benchmark(euclidean, NCALLS_B, ARRAYSIZE_B)

    #
    # Print report line
    #
    print(FMTSTR.format(name, time_taken_a, baseline_a /
                        time_taken_a, time_taken_b, baseline_b / time_taken_b))
