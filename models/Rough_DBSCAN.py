
from models.Counted_Leaders import Counted_Leaders
from models.DBSCAN import DBSCAN
import numpy as np


class Rough_DBSCAN:
    def __init__(self, epsilon, minPts, radius):

        # Prepare DBSCAN
        self.dbscan = DBSCAN(epsilon, minPts)

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


    def fit(self, D, verbose=True):

        # Prepare counted leaders
        lstar = Counted_Leaders(D, self.radius)
        self.leaders = np.array(lstar.L)
        self.followers = lstar.followers
        self.counts = lstar.count
        self.ids = lstar.ids

        # Fit classification with leaders
        pi = self.dbscan.fit(self.leaders, verbose=verbose)

        # Substitute leaders with followers
        classification = np.zeros(shape=(D.shape[0]))
        for x, c in zip(self.leaders, pi):
            classification[self.ids[tuple(x)]] = c

        return classification


    def predict(self):
        pass