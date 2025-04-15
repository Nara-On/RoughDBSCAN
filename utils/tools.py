
import numpy as np
from scipy.cluster.hierarchy import leaders
from scipy.spatial.distance import euclidean
import pprint


def coincidence(main, lookup):
    # When there are many such leaders then choose the first one
    # according to the ordering in which the set L is created.
    for m in main:
        for s in lookup:
            if np.array_equal(m, s):
                return s


def find_N(i, D, e):
    distances = [euclidean(i, t) for t in D]
    return np.where([d<=e for d in distances])[0]


def find_rough_N(l, L, counts, distances, e):
    Nr = 0
    ind = np.where([d<=e for d in distances[l,:]])[0]
    for i in ind:
        Nr += counts[tuple(L[i])]
    return Nr, ind
