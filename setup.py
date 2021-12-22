#!/usr/bin/env python3
from distutils.core import setup
from Cython.Build import cythonize
import os

os.environ['CFLAGS'] = '-Ofast -march=native -mtune=native'
setup(ext_modules=cythonize('pyxeuclid.pyx'))
