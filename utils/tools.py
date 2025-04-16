
import numpy as np


def coincidence(main, lookup):
    # When there are many such leaders then choose the first one
    # according to the ordering in which the set L is created.
    for m in main:
        for s in lookup:
            if np.array_equal(m, s):
                return s


def find_N(i, D, distances, e):
    ind = np.where([d <= e for d in distances[i, :]])[0]
    return len(ind), ind


def find_rough_N(l, L, counts, distances, e):
    Nr = 0
    ind = np.where([d<=e for d in distances[l,:]])[0]
    for i in ind:
        Nr += counts[tuple(L[i])]
    return Nr, ind
