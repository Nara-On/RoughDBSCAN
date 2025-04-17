
import os
import time
import pandas as pd
import numpy as np

from experiments.experiment_blobs import sizes
from models.Rough_DBSCAN import Rough_DBSCAN
from models.DBSCAN import DBSCAN
#from sklearn.cluster import DBSCAN
from models.Counted_Leaders import Counted_Leaders
from sklearn.metrics.cluster import rand_score

from utils.plots import generate_single_plots, plot_leaders, plot_leader_count


def test(X, Y, epsilon, minPts, radius, name_experiment,
               root_saving="../visuals/", plots=True, verbose=True):

    if verbose:
        print("\nStarting RoughDBSCAN")
        print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}, Radius={radius}")
    rdbscan = Rough_DBSCAN(epsilon, minPts, radius)

    if verbose:
        print("Fitting...")

    toR = time.time()
    predictR = rdbscan.fit_predict(X, verbose=verbose)
    tfR = time.time() - toR

    if verbose:
        print(predictR)
        print("\nStarting DBSCAN")
        print(f"Parameters: Epsilon={epsilon}, MinPts={minPts}")
    dbscan = DBSCAN(epsilon, minPts)

    if verbose:
        print("Fitting...")
    toD = time.time()
    predictD = dbscan.fit_predict(X, timelimit=3600, verbose=verbose)
    tfD = time.time() - toD

    if verbose:
        print(predictD)
        print("\nPlotting results")

    if plots:
        generate_single_plots(X, Y, rdbscan.leaders, predictD, predictR, tfD, tfR,
                              epsilon, minPts, radius, name_experiment, root_saving=root_saving)

    return dbscan, rdbscan, predictD, predictR, tfD, tfR



def experiment(epsilons, minPts, rs, sizes, dataset,
               name_experiment, root_saving="../visuals/", verbose=True):

    root = root_saving
    if not os.path.exists(root):
        os.makedirs(root)

    column_names = ["Size", "Epsilon", "MinPts", "Radius", "Leaders", "Leaders Count",
                    "Classification RoughDBSCAN", "Classification DBSCAN",
                    "Rand-Index RoughDBSCAN", "Rand-Index DBSCAN", "Time RoughDBSCAN", "Time DBSCAN"]

    results = pd.DataFrame(columns=column_names)

    it = 0
    iterations = len(epsilons) * len(minPts) * len(rs) * len(sizes)

    for s in sizes:
        X,Y = dataset(s, verbose=verbose)

        for e in epsilons:
            for pts in minPts:
                for r in rs:

                    if verbose:
                        print(f"Experiment {it+1} of {iterations}: {round((it+1)/iterations*100,2)}%")

                    dbscan, rdbscan, predictD, predictR, tfD, tfR = test(X=X, Y=Y, epsilon=e, minPts=pts, radius=r,
                           name_experiment=f"{s}_E{e}_T{pts}_R{r}", root_saving=root_saving, plots=False, verbose=verbose)

                    if dbscan.timelimit is not None:
                        tfD = 3600 # Default One Hour Limit Exceeded

                    results_experiment = pd.Series({
                        "Size": s,
                        "Epsilon": e,
                        "MinPts": pts,
                        "Radius": r,

                        "Leaders": np.array(rdbscan.leaders),
                        "Leaders Count": len(rdbscan.leaders),

                        "Classification RoughDBSCAN": predictR,
                        "Classification DBSCAN": predictD,

                        "Rand-Index RoughDBSCAN": rand_score(Y, predictR),
                        "Rand-Index DBSCAN": rand_score(Y, predictD),

                        "Time RoughDBSCAN": tfR,
                        "Time DBSCAN": tfD
                    })

                    results.loc[len(results)] = results_experiment
                    results.to_csv(root_saving + name_experiment + ".csv", index=False)
                    it += 1
    return results


def experiment_leaders(datasets, root_saving="../visuals/", plots=True, verbose=True):

    column_names = ["Name", "Size", "Radius", "Leaders", "Leaders Count", "Time"]
    results = pd.DataFrame(columns=column_names)

    it = 0
    iterations = 1
    for its in datasets:
        iterations *= len(its[2]) * len(its[3])

    for name, data, sizes, radius in datasets:
        for s in sizes:
            for r in radius:

                if verbose:
                    print(f"Experiment {it + 1} of {iterations}: {round((it + 1) / iterations * 100, 2)}%")

                X,Y = data(s, verbose)

                to = time.time()
                leaders = np.array(Counted_Leaders(X, r))
                tf = time.time() - to

                results_experiment = pd.Series({
                    "Name": name,
                    "Size": s,
                    "Radius": r,
                    "Leaders": leaders,
                    "Leaders Count": len(leaders),
                    "Time DBSCAN": tf
                })

                results.loc[len(results)] = results_experiment
                results.to_csv(root_saving + name + ".csv", index=False)

                if plots:
                    plot_leaders(X, Y, leaders, r, root_saving + f"leader_{name}_{s}_{r}")

                it += 1

    if plots:
        plot_leader_count(results, root_saving + "results_leaders_patterns")