
from utils.datasets import blobs
from utils.experiments import experiment

root_saving = "../visuals/blobs/"


if __name__ == "__main__":

    # Hyperparameters
    n_samples = 1000
    centers = 3
    cluster_std = 0.5

    epsilon = 2.45
    minPts = 30
    radius = 0.4


    # Execute experiments
    X, Y = blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)
    experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius, root_saving=root_saving)