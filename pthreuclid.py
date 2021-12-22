
# pythran export dist(float64[:], float64[:])


def dist(x, y):
    """ Pure python implementation of euclidean distance formula. """
    dist = 0.0
    for i in range(len(x)):
        dist += (x[i] - y[i])**2
    return dist**0.5
