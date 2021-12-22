

cpdef double dist(double [:] x, double [:] y):
    cdef double dist
    cdef int i
    dist = 0.0
    for i in range(len(x)):
        dist += (x[i] - y[i])**2
    return dist**0.5
