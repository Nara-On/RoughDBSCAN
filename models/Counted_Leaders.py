
#from kemlglearn.cluster import Leader
from scipy.spatial.distance import euclidean
from utils.tools import coincidence


class Counted_Leaders:

    def __init__(self, X, radius):
        self.X = X
        self.radius = radius
        self.__call__()

    def __call__(self):
        L = []
        followers = {}
        count = {}

        for x in self.X:
            candidates = []
            for l in L:
                if euclidean(x, l) < self.radius:
                    candidates.append(l)

            if candidates == [] or L == []:
                L.append(x)
                followers[x.tobytes()] = [x]
                count[x.tobytes()] = 1
            else:
                leader = coincidence(L, candidates).tobytes()
                followers[leader].append(x)
                count[leader] += 1

        return L, followers, count