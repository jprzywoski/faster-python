#!/usr/bin/env bash

swig -python cdist.i
gcc -c -fPIC cdist.c cdist_wrap.c -lm -I/usr/include/python3.6m -I/home/jakub/.local/lib/python3.6/site-packages/numpy/core/include
ld -shared cdist.o cdist_wrap.o -o _cdist.so
