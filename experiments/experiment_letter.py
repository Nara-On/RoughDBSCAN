
from utils.datasets import letter
from utils.experiments import experiment

root_saving = "../visuals/letter/"

e = 0.5
minPts = 8
t = [0.4, 0.35, 0.3, 0.25]

sizes = [2000, 4000, 6000, 8000, 10000]


if __name__ == "__main__":

    # Hyperparameters
    size = 2000

    epsilon = 0.5
    minPts = 8
    radius = 0.25

    plots = False


    # Test code
    X, Y = letter(size)
    experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
               name_experiment=f"{size}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=plots)