#!/usr/bin/env bash

gcc -Ofast -march=native -mtune=native -lm -shared cdist.c -o libdist.so
