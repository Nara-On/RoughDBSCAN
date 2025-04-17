
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.cluster import rand_score


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
                       root + f"/metrics_models_" + name_experiment + ".jpg")


def plot_leader_count(leaders_list, savePath):

    n_plots = len(leaders_list)
    rows = math.ceil(n_plots / 2)
    columns = n_plots - rows

    fig, ax = plt.subplots(rows, columns, figsize=(10, 5))

    for i, name, results in enumerate(leaders_list):
        thresholds = results["Radius"]

        #thresholds = np.unique(results["Radius"])
        #for th in thresholds:
        #   leader_count = results.loc[results["Radius"] == th, "Leaders Count"]
        #   sizes = results.loc[results["Radius"] == th, "Size"]
        #   scatter = ax[i].scatter(sizes, leader_count, label=th)

        leader_count = results["Leaders Count"]
        sizes = results["Size"]
        ax[i].scatter(sizes, leader_count, label=thresholds)

        ax[i].legend()
        ax[i].set_title(results["Name"])

    plt.tight_layout()
    plt.savefig(savePath)
