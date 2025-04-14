
from models.Rough_DBSCAN import Rough_DBSCAN
from utils.metrics import generate_results
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

import time

root_saving = "../visuals/blobs/"



if __name__ == "__main__":

    print("\n-------- Starting Test --------\n")
    n_samples = 1000
    centers = 4
    cluster_std = 0.5

    epsilon = 4
    minPts = 10
    radius = 0.45


    print("Generating BLOBS dataset")
    X, Y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)


    print("Starting RoughDBSCAN")
    print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}, Radius={radius}")
    rdbscan = Rough_DBSCAN(epsilon, minPts, radius)

    print("Fitting...")
    toR = time.time()
    predictR = rdbscan.fit_predict(X)
    tfR = time.time() - toR
    print(predictR)


    print("\nStarting DBSCAN")
    print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}")
    dbscan = DBSCAN(eps=epsilon, min_samples=minPts)

    print("Fitting...")
    toD = time.time()
    predictD = dbscan.fit_predict(X)
    tfD = time.time() - toD
    print(predictD)


    print("\nPlotting results")
    generate_results(X, Y, predictR, rdbscan.leaders, tfR, predictD, tfD,
                     epsilon, minPts, radius, root_saving)