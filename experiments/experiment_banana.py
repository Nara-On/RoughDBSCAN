
from models.Rough_DBSCAN import Rough_DBSCAN
from utils.metrics import generate_results
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

import time

root_saving = "../visuals/banana/"



if __name__ == "__main__":

    print("\n-------- Starting Test --------\n")
    n_samples = 4000
    noise = 0.05

    epsilon = 2
    minPts = 3
    radius = 0.2

    print("Generating BANANA dataset")
    X, Y = make_moons(n_samples=n_samples, noise=noise, random_state=0)


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