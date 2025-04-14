
import os
import matplotlib.pyplot as plt

from sklearn.metrics.cluster import rand_score


def metrics_paper(y, predict):
    return rand_score(y, predict)


def generate_results(X, Y, predictR, leaders, tfR, predictD, tfD,
                     epsilon, minPts, radius, root_saving="../visuals/", cmap_plots="cividis"):

    # Create folder
    if not os.path.exists(root_saving):
        os.makedirs(root_saving)


    # Results RDBSCAN
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    scatter1 = ax1.scatter(X[:, 0], X[:, 1], c=predictR, cmap=cmap_plots, label=predictR)
    ax1.set_title(f"Rough DBSCAN")
    ax1.legend(*scatter1.legend_elements())

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
    ax1.set_title(f"Classification: Epsilon={epsilon}, MinPts={minPts}, Radius={radius}")
    ax1.legend(*scatter1.legend_elements())
    ax1.set_title("Rough DBSCAN")

    scatter2 = ax2.scatter(X[:, 0], X[:, 1], c=predictD, cmap=cmap_plots, label=predictD)
    ax2.set_title(f"Classification: Epsilon={epsilon}, MinPts={minPts}")
    ax2.legend(*scatter2.legend_elements())
    ax2.set_title("DBSCAN")

    ax3.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_plots)
    ax3.set_title("True values")

    plt.tight_layout()
    plt.savefig(root_saving + "comparison_models.jpg")