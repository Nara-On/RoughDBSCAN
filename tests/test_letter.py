
from utils.datasets import letter
from utils.experiments import test

root_saving = "../visuals/tests/letter/"


if __name__ == "__main__":

    # Hyperparameters
    size = 2000

    epsilon = 0.5
    minPts = 8
    radius = 0.25

    plots = True


    # Test code
    X, Y = letter(size)
    test(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
               name_experiment=f"{size}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=plots)