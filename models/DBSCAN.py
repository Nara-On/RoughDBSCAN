import time

import numpy as np
from utils.tools import find_N
from utils.tools import find_rough_N
from scipy.spatial.distance import cdist


class DBSCAN:
    def __init__(self, epsilon, minPts):
        self.epsilon = epsilon
        self.minPts = minPts

        self.labels = None
        self.timelimit = None


    def fit(self, D, timelimit=None, verbose=True):

        # Limit execution time to an hour
        t0 = 0
        limit = False
        self.timelimit = timelimit

        if timelimit is not None:
            t0 = time.time()
            limit = True


        # DBSCAN
        cid = 0

        classification = np.zeros(shape=(D.shape[0]))  # -1=Noise, 0=Init, Else=Cluster
        markings = np.zeros((D.shape[0]))  # 0=Unseen, 1=Seen
        distance_matrix = cdist(D, D, 'euclidean')

        for i, x in enumerate(D):

            if verbose:
                print(f"Sample {i + 1} of {D.shape[0]}: {round((i + 1) / D.shape[0] * 100, 2)}%")

            # If x is not marked as "seen"
            if markings[i] != 1:

                # Mark x as "seen"
                markings[i] = 1

                # Find subset of patterns in D that are present in the hyper-sphere of radius e at x
                N, indN = find_N(i, D, distance_matrix, self.epsilon)

                if N < self.minPts:
                    # Mark x as "noise"
                    classification[i] = -1

                else:
                    # Mark x as "seen"
                    markings[i] = 1
                    cid += 1

                    # Mark each pattern of N with cluster identifier cid
                    classification[indN] = cid

                    # Add each pattern of N which is not marked as "seen"
                    q = list(indN[np.where(markings[indN] != 1.0)[0]])

                    while q:
                        # Take pattern y from queue and mark it as "seen"; Remove y from queue
                        j = q.pop(0)
                        markings[j] = 1

                        M, indM = find_N(j, D, distance_matrix, self.epsilon)

                        if M > self.minPts:
                            # Mark each pattern of M with cluster identifier cid
                            # If any pattern of M is marked as "noise" then remove this mark.
                            classification[indM] = cid

                            # Add each pattern of M which is not marked as "seen" to the list queue
                            q.extend(list(indM[np.where(markings[indM] != 1.0)[0]]))

                        if limit and (timelimit < (time.time() - t0)):
                            self.labels = classification
                            return 1

        self.labels = classification


    def rough_fit(self, L, counts, verbose=True):

        cid = 0

        classification = np.zeros(shape=(L.shape[0])) #-1=Noise, 0=Init, Else=Cluster
        markings = np.zeros((L.shape[0])) # 0=Unseen, 1=Seen
        distance_matrix = cdist(L, L, 'euclidean')


        for i, x in enumerate(L):

            if verbose:
                print(f"Leader {i+1} of {L.shape[0]}: {round((i+1)/L.shape[0]*100,2)}%")

            # If x is not marked as "seen"
            if markings[i] != 1:

                # Mark x as "seen"
                markings[i] = 1

                # Find subset of patterns in D that are present in the hyper-sphere of radius e at x
                N, indN = find_rough_N(i, L, counts, distance_matrix, self.epsilon)

                if N < self.minPts:
                    # Mark x as "noise"
                    classification[i] = -1

                else:
                    # Mark x as "seen"
                    markings[i] = 1
                    cid += 1

                    # Mark each pattern of N with cluster identifier cid
                    classification[indN] = cid

                    # Add each pattern of N which is not marked as "seen"
                    q = list(indN[np.where(markings[indN] != 1.0)[0]])

                    while q:
                        # Take pattern y from queue and mark it as "seen"; Remove y from queue
                        j = q.pop(0)
                        markings[j] = 1

                        M, indM = find_rough_N(j, L, counts, distance_matrix, self.epsilon)

                        if M > self.minPts:
                            # Mark each pattern of M with cluster identifier cid
                            # If any pattern of M is marked as "noise" then remove this mark.
                            classification[indM] = cid

                            # Add each pattern of M which is not marked as "seen" to the list queue
                            q.extend(list(indM[np.where(markings[indM] != 1.0)[0]]))

        self.labels = classification


    def fit_predict(self, D, timelimit=None, verbose=True):
        self.fit(D, timelimit, verbose)
        return self.labels


    def rough_fit_predict(self, L, counts, verbose=True):
        self.rough_fit(L, counts, verbose)
        return self.labels