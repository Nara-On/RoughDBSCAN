
from models.Counted_Leaders import Counted_Leaders
from models.DBSCAN import DBSCAN_scratch
import numpy as np


class Rough_DBSCAN:
    def __init__(self, epsilon, minPts, radius):

        # Prepare DBSCAN
        self.dbscan = DBSCAN_scratch(epsilon, minPts)

        # Save parameters
        self.epsilon = epsilon
        self.minPts = minPts
        self.radius = radius

        # Prepare parameters
        self.leaders = None
        self.followers = None
        self.follower_ids = None
        self.counts = None
        self.ids = None
        self.labels = None


    def fit(self, D, verbose=True):

        # Prepare counted leaders
        if verbose:
            print("Finding leaders...")
        lstar = Counted_Leaders(D, self.radius)
        self.leaders = np.array(lstar.L)
        self.followers = lstar.followers
        self.counts = lstar.count
        self.ids = lstar.ids


        # Fit DBSCAN with leaders
        pi = self.dbscan.rough_fit_predict(self.leaders, self.counts, verbose=verbose)

        # Substitute leaders with followers
        classification = np.zeros(shape=(D.shape[0]))
        for x, c in zip(self.leaders, pi):
            classification[self.ids[tuple(x)]] = c

        self.labels = classification


    def fit_predict(self, D, verbose=True):
        self.fit(D, verbose)
        return self.labels