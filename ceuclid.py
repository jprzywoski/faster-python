import ctypes
from numpy.ctypeslib import ndpointer

lib = ctypes.cdll.LoadLibrary('./libdist.so')
fn = lib.cdist
fn.restype = ctypes.c_double
fn.argtypes = [
    ndpointer(ctypes.c_double),
    ndpointer(ctypes.c_double),
    ctypes.c_size_t
]


def dist(x, y):
    return fn(x, y, len(x))
