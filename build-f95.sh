#!/usr/bin/env bash

python3 -m numpy.f2py -c --opt='-Ofast -march=native -mtune=native' forteuclid.f95 -m forteuclid
