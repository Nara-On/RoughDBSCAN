
import os
import time
import matplotlib.pyplot as plt

from models.Rough_DBSCAN import Rough_DBSCAN
from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import rand_score


def experiment(X, Y, epsilon, minPts, radius, root_saving="../visuals/", verbose=True):

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
    dbscan = DBSCAN(eps=epsilon, min_samples=minPts)

    if verbose:
        print("Fitting...")
    toD = time.time()
    predictD = dbscan.fit_predict(X)
    tfD = time.time() - toD

    if verbose:
        print(predictD)
        print("\nPlotting results")

    generate_plots(X, Y, predictR, rdbscan.leaders, tfR, predictD, tfD,
                   radius, root_saving=root_saving)


def generate_plots(X, Y, predictR, leaders, tfR, predictD, tfD,
                   radius, root_saving="../visuals/", cmap_plots="cividis"):

    # Create folder
    if not os.path.exists(root_saving):
        os.makedirs(root_saving)


    # Results RDBSCAN
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
    plt.savefig(root_saving + "rdbscan_all.jpg")


    # Leaders RDBSCAN
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_plots)
    for pts in leaders:
        ax.scatter(pts[0], pts[1], c="crimson")
        circle = plt.Circle(xy=(pts[0], pts[1]), radius=radius, color="crimson", alpha=0.25)
        ax.add_patch(circle)
    ax.set_title("Leaders")

    plt.tight_layout()
    plt.savefig(root_saving + "rdbscan_leaders.jpg")


    # Results DBSCAN vs RDBSCAN
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
    plt.savefig(root_saving + "comparison_models.jpg")


    # Metrics DBSCAN vs RDBSCAN
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    bar1 = ax1.bar(["Rough DBSCAN", "DBSCAN"], [rand_score(Y, predictR), rand_score(Y, predictD)], color=["tab:orange", "tab:cyan"])
    ax1.bar_label(bar1, fmt='%.2f')
    ax1.set_ylim([0, 1])
    ax1.set_title("Rand Index")

    bar2 = ax2.bar(["Rough DBSCAN", "DBSCAN"], [tfR, tfD], color=["tab:orange", "tab:cyan"])
    ax2.bar_label(bar2, fmt='%.2f')
    ax2.set_title("Time")

    plt.tight_layout()
    plt.savefig(root_saving + "metrics_models.jpg")