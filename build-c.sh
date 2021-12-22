#!/usr/bin/env bash

gcc -Ofast -march=native -mtune=native -shared cdist.c -o libdist.so
