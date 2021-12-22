import numpy as np

def dist(x, y):
    """ Numpy implementation. """
    return np.sqrt(np.sum(np.power(x-y, 2)))
