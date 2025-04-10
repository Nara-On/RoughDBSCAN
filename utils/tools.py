
import numpy as np
from scipy.spatial.distance import euclidean


def coincidence(main, search):
    # When there are many such leaders then choose the first one according to the ordering in which the set L is created.
    for m in main:
        for s in search:
            if np.array_equal(m, s):
                return s


def find_N(l, L, e):
    distances = [euclidean(l, t) for t in L]
    #return np.where([False if d==0 else d<=e for d in distances])[0]
    return np.where([d<=e for d in distances])[0]
