
import os
import time
import matplotlib.pyplot as plt

from models.Rough_DBSCAN import Rough_DBSCAN
from models.DBSCAN import DBSCAN
#from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import rand_score


def experiment(X, Y, epsilon, minPts, radius, name_experiment,
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
    predictD = dbscan.fit_predict(X)
    tfD = time.time() - toD

    if verbose:
        print(predictD)
        print("\nPlotting results")

    if plots:
        generate_single_plots(X, Y, rdbscan.leaders, predictD, predictR, tfD, tfR,
                              epsilon, minPts, radius, name_experiment, root_saving=root_saving)

    return dbscan, rdbscan, predictD, predictR, tfD, tfR



def plot_RDBSCAN(X, Y, leaders, radius, predictR, savePath, cmap_plots="cividis"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    scatter1 = ax1.scatter(X[:, 0], X[:, 1], c=predictR, cmap=cmap_plots, label=predictR)
    ax1.legend(*scatter1.legend_elements())
    ax1.set_title("Rough DBSCAN")

    ax2.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_plots)
    for pts in leaders:
        ax2.scatter(pts[0], pts[1], c="crimson")
        circle = plt.Circle(xy=(pts[0], pts[1]), radius=radius, color="crimson", alpha=0.25)
        ax2.add_patch(circle)
    ax2.set_title("Leaders")

    ax3.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_plots)
    ax3.set_title("True values")

    plt.tight_layout()
    plt.savefig(savePath)


def plot_leaders(X, Y, leaders, radius, savePath, cmap_plots="cividis"):
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_plots)
    for pts in leaders:
        ax.scatter(pts[0], pts[1], c="crimson")
        circle = plt.Circle(xy=(pts[0], pts[1]), radius=radius, color="crimson", alpha=0.25)
        ax.add_patch(circle)
    ax.set_title("Leaders")

    plt.tight_layout()
    plt.savefig(savePath)


def plot_DBSCANnRDBSCAN(X, Y, predictD, predictR, savePath, cmap_plots="cividis"):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    scatter1 = ax1.scatter(X[:, 0], X[:, 1], c=predictR, cmap=cmap_plots, label=predictR)
    ax1.legend(*scatter1.legend_elements())
    ax1.set_title("Rough DBSCAN")

    scatter2 = ax2.scatter(X[:, 0], X[:, 1], c=predictD, cmap=cmap_plots, label=predictD)
    ax2.legend(*scatter2.legend_elements())
    ax2.set_title("DBSCAN")

    ax3.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_plots)
    ax3.set_title("True values")

    plt.tight_layout()
    plt.savefig(savePath)


def plot_metrics_paper(Y, predictD, predictR, tfD, tfR, savePath):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    bar1 = ax1.bar(["Rough DBSCAN", "DBSCAN"], [rand_score(Y, predictR), rand_score(Y, predictD)], color=["tab:orange", "tab:cyan"])
    ax1.bar_label(bar1, fmt='%.2f')
    ax1.set_ylim([0.0, 1.0])
    ax1.set_title("Rand Index")

    bar2 = ax2.bar(["Rough DBSCAN", "DBSCAN"], [tfR, tfD], color=["tab:orange", "tab:cyan"])
    ax2.bar_label(bar2, fmt='%.2f')
    ax2.set_title("Time")

    plt.tight_layout()
    plt.savefig(savePath)



def generate_single_plots(X, Y, leaders, predictD, predictR, tfD, tfR,
                          epsilon, minPts, radius, name_experiment,
                          root_saving="../visuals/", cmap_plots="cividis"):

    # Create folder
    root = root_saving + "/" + name_experiment
    if not os.path.exists(root):
        os.makedirs(root)


    # Results RDBSCAN
    plot_RDBSCAN(X, Y, leaders, radius, predictR,
                 root + f"/rdbscan_all_" + name_experiment + ".jpg", cmap_plots)

    # Leaders RDBSCAN
    plot_leaders(X, Y, leaders, radius, root + f"/rdbscan_leaders_" + name_experiment + ".jpg", cmap_plots)

    # Results DBSCAN vs RDBSCAN
    plot_DBSCANnRDBSCAN(X, Y, predictD, predictR,
                        root + f"/comparison_models_" + name_experiment + ".jpg", cmap_plots)

    # Metrics DBSCAN vs RDBSCAN
    plot_metrics_paper(Y, predictD, predictR, tfD, tfR,
                       root + f"/metrics_models_" + name_experiment + ".jpg",)