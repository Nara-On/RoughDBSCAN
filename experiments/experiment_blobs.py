
from models.Rough_DBSCAN import Rough_DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt



if __name__ == "__main__":

    print("-------- Starting Test --------\n")
    n_samples = 1000
    centers = 4
    cluster_std = 0.5

    epsilon = 4
    minPts = 10
    radius = 0.45


    print("Generating dataset...")
    X, Y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)

    print("\nStarting Classification...")
    rdbscan = Rough_DBSCAN(epsilon, minPts, radius)

    print("\nFitting...")
    classification = rdbscan.fit(X)
    print(classification)

    print("\nPlotting results...")
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    scatter1 = ax1.scatter(X[:, 0], X[:, 1], c=classification, cmap="cividis", label=classification)
    ax1.set_title(f"Classification: Epsilon={epsilon}, MinPts={minPts}, Radius={radius}")
    ax1.legend(*scatter1.legend_elements())

    ax2.scatter(X[:, 0], X[:, 1], c=Y, cmap="cividis")
    for pts in rdbscan.leaders:
        ax2.scatter(pts[0], pts[1], c="crimson")
        circle = plt.Circle(xy=(pts[0], pts[1]), radius=radius, color="crimson", alpha=0.25)
        ax2.add_patch(circle)
    ax2.set_title("Leaders")

    ax3.scatter(X[:, 0], X[:, 1], c=Y, cmap="cividis")
    ax3.set_title("Banana dataset")

    plt.tight_layout()

    print("Saving figure...")
    plt.savefig("../visuals/experiment_blobs.jpg")