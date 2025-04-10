
import numpy as np
from utils.tools import find_N


class DBSCAN:
    def __init__(self, epsilon, minPts):
        self.epsilon = epsilon
        self.minPts = minPts


    def fit(self, D, verbose=True):

        cid = 0

        classification = np.zeros(shape=(D.shape[0])) #-1=Noise, 0=Init, Else=Cluster
        markings = np.zeros((D.shape[0])) # 0=Unseen, 1=Seen

        for i, x in enumerate(D):

            if verbose:
                print(f"Sample {i+1} of {D.shape[0]}: {round((i+1)/D.shape[0]*100,2)}%")

            # If x is not marked as "seen"
            if markings[i] != 1:

                # Mark x as "seen"
                markings[i] = 1

                # Find subset of patterns in D that are present in the hyper-sphere of radius e at x
                N = find_N(x, D, self.epsilon)

                if len(N) < self.minPts:
                    # Mark x as "noise"
                    classification[i] = -1

                else:
                    # Mark x as "seen"
                    markings[i] = 1
                    cid += 1

                    # Mark each pattern of N with cluster identifier cid
                    classification[N] = cid

                    # Add each pattern of N which is not marked as "seen"
                    q = list(N[np.where(markings[N] != 1.0)[0]])

                    while q:
                        # Take pattern y from queue and mark it as "seen"; Remove y from queue
                        j = q.pop(0)
                        y = D[j]
                        markings[j] = 1

                        M = find_N(y, D, self.epsilon)

                        if len(M) > self.minPts:
                            # Mark each pattern of M with cluster identifier cid
                            # If any pattern of M is marked as "noise" then remove this mark.
                            classification[M] = cid

                            # Add each pattern of M which is not marked as "seen" to the list queue
                            q.extend(list(N[np.where(markings[N] != 1.0)[0]]))

        return classification


    def predict(self, X):
        pass
