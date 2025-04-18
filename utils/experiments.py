
import os
import time
import pandas as pd
import numpy as np

from models.Rough_DBSCAN import Rough_DBSCAN
from models.DBSCAN import DBSCAN_scratch
from sklearn.cluster import DBSCAN
from models.Counted_Leaders import Counted_Leaders

from sklearn.metrics.cluster import rand_score
from utils.plots import generate_single_plots, plot_leader_count



def test_RDBSCAN(X, epsilon, minPts, radius, verbose=True):
    if verbose:
        print("\nStarting RoughDBSCAN")
        print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}, Radius={radius}")
    rdbscan = Rough_DBSCAN(epsilon, minPts, radius)

    if verbose:
        print("Fitting...")

    toR = time.time()
    predictR = rdbscan.fit_predict(X, verbose=verbose)
    tfR = time.time() - toR

    return rdbscan, predictR, tfR


def test_DBSCAN_scratch(X, epsilon, minPts, verbose=True):
    if verbose:
        print("\nStarting DBSCAN")
        print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}")
    dbscan = DBSCAN_scratch(epsilon, minPts)

    if verbose:
        print("Fitting...")
    toD = time.time()
    predictD = dbscan.fit_predict(X, timelimit=3600, verbose=verbose)
    tfD = time.time() - toD

    return dbscan, predictD, tfD


def test_DBSCAN_sklearn(X, epsilon, minPts, verbose=True):
    if verbose:
        print("\nStarting DBSCAN")
        print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}")
    dbscan = DBSCAN(eps=epsilon, min_samples=minPts)

    if verbose:
        print("Fitting...")
    toD = time.time()
    predictD = dbscan.fit_predict(X)
    tfD = time.time() - toD

    return dbscan, predictD, tfD


def test(X, Y, epsilon, minPts, radius, name_experiment,
               root_saving="../visuals/", plots=True, sklearn=False, verbose=True):

    rdbscan, predictR, tfR = test_RDBSCAN(X, epsilon, minPts, radius, verbose=True)

    if sklearn:
        dbscan, predictD, tfD = test_DBSCAN_sklearn(X, epsilon, minPts, verbose=True)
    else:
        dbscan, predictD, tfD = test_DBSCAN_scratch(X, epsilon, minPts, verbose=True)

    if plots:
        if verbose:
            print("\nPlotting results")
        generate_single_plots(X, Y, rdbscan.leaders, predictD, predictR, tfD, tfR,
                              radius, name_experiment, root_saving=root_saving)

    return dbscan, rdbscan, predictD, predictR, tfD, tfR



def experiment(epsilons, minPts, rs, sizes, dataset,
               name_experiment, root_saving="../visuals/", sklearn=False, verbose=True):

    # Create Directory
    root = root_saving
    if not os.path.exists(root):
        os.makedirs(root)

    # Create Results DataFrame
    column_names = ["Size", "Epsilon", "MinPts", "Radius", "Leaders", "Leaders Count",
                    "Classification RoughDBSCAN", "Classification DBSCAN",
                    "Rand-Index RoughDBSCAN", "Rand-Index DBSCAN", "Time RoughDBSCAN", "Time DBSCAN"]

    results = pd.DataFrame(columns=column_names)

    # Verbose reparations
    iterations = len(epsilons) * len(rs) * len(sizes)

    # Start Experiment
    it = 0
    for s, pts in zip(sizes, minPts):
        X,Y = dataset(s, verbose=verbose)

        for e in epsilons:

            results_RDBSCAN = []
            for r in rs:
                if verbose:
                    print(f"Experiment RDBSCAN {it+1} of {iterations}: {round((it+1)/iterations*100,2)}%")
                rdbscan, predictR, tfR = test_RDBSCAN(X=X, epsilon=e, minPts=pts, radius=r, verbose=verbose)
                results_RDBSCAN.append([rdbscan, predictR, tfR])
                it += 1

            if verbose:
                print(f"Experiment DBSCAN {it + 1} of {iterations}: {round((it + 1) / iterations * 100, 2)}%")

            if sklearn:
                dbscan, predictD, tfD = test_DBSCAN_sklearn(X, e, pts, verbose=verbose)
            else:
                dbscan, predictD, tfD = test_DBSCAN_scratch(X, e, pts, verbose=verbose)
                if dbscan.timelimit is not None:
                    tfD = 3600  # Default One Hour Limit Exceeded
            it += 1


            # Save values: RDBSCAN (all rs) with Same DBSCAN
            if verbose:
                print("Checkpoint: Saving sets of experiments")
            for rough, preds, t in results_RDBSCAN:
                results_experiment = pd.Series({
                    "Size": s,
                    "Epsilon": e,
                    "MinPts": pts,
                    "Radius": rough.radius,

                    "Leaders": np.array(rough.leaders),
                    "Leaders Count": len(rough.leaders),

                    "Classification RoughDBSCAN": preds,
                    "Classification DBSCAN": predictD,

                    "Rand-Index RoughDBSCAN": rand_score(Y, preds),
                    "Rand-Index DBSCAN": rand_score(Y, predictD),

                    "Time RoughDBSCAN": t,
                    "Time DBSCAN": tfD
                })
                results.loc[len(results)] = results_experiment
                results.to_csv(root_saving + name_experiment + ".csv", index=False)

    return results



def experiment_counted_leaders(datasets, root_saving="../visuals/", plots=True, verbose=True):

    # Create Directory
    root = root_saving
    if not os.path.exists(root):
        os.makedirs(root)

    # Create Results DataFrame
    column_names = ["Name", "Size", "Radius", "Leaders", "Leaders Count", "Time"]
    results = pd.DataFrame(columns=column_names)

    # Verbose preparations
    iterations = 0
    for its in datasets:
        iterations += len(its[2]) * len(its[3])

    # Start experiment
    it = 0
    for name, data, sizes, radius in datasets:
        for s in sizes:
            X, Y = data(s, verbose)

            for r in radius:

                if verbose:
                    print(f"Experiment {it + 1} of {iterations}: {round((it + 1) / iterations * 100, 4)}%")

                to = time.time()
                leaders = Counted_Leaders(X, r).L
                tf = time.time() - to

                results_experiment = pd.Series({
                    "Name": name,
                    "Size": s,
                    "Radius": r,
                    "Leaders": leaders,
                    "Leaders Count": len(leaders),
                    "Time": tf
                })

                results.loc[len(results)] = results_experiment
                results.to_csv(root_saving + "results_leaders_patterns.csv", index=False)
                it += 1

    if plots:
        plot_leader_count(results, root_saving + "results_leaders_patterns.jpg")