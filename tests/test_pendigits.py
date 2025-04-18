
from utils.datasets import pendigits
from utils.experiments import test

root_saving = "../visuals/tests/pendigits/"


if __name__ == "__main__":

    # Hyperparameters
    size = 1000

    epsilon = 40
    minPts = 4
    radius = 15


    # Execute experiments
    X, Y = pendigits(size)
    test(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
         name_experiment=f"{size}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=True)