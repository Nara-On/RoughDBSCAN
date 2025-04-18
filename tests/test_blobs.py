
from utils.datasets import blobs
from utils.experiments import test

root_saving = "../visuals/tests/blobs/"


if __name__ == "__main__":

    # Hyperparameters
    n_samples = 1000
    centers = 3
    cluster_std = 0.5

    epsilon = 0.5
    minPts = 30
    radius = 0.5

    plots = True


    # Execute experiments
    X, Y = blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)
    test(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
               name_experiment=f"{n_samples}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=plots)
    # plot_dataset(X, Y, "Blobs", "../visuals/blobs.jpg")