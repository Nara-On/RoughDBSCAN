
from scipy.spatial.distance import euclidean
from utils.tools import coincidence

import numpy as np


class Counted_Leaders:

    def __init__(self, D, radius):
        self.D = D
        self.radius = radius
        self.__call__()

    def __call__(self):
        L = []
        followers = {}
        ids = {}
        count = {}

        for i, x in enumerate(self.D):
            candidates = []
            for j in L:
                if euclidean(x, j) < self.radius:
                    candidates.append(j)

            if candidates == [] or L == []:
                L.append(x)
                followers[tuple(x)] = [x]
                ids[tuple(x)] = [i]
                count[tuple(x)] = 1
            else:
                leader = coincidence(L, candidates)
                followers[tuple(leader)].append(x)
                ids[tuple(leader)].append(i)
                count[tuple(leader)] += 1

        self.L = L
        self.followers = followers
        self.count = count
        self.ids = ids