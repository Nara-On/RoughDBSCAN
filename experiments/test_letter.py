
from utils.datasets import letter
from utils.experiments import experiment

root_saving = "../visuals/letter/"


if __name__ == "__main__":

    # Hyperparameters
    n_samples = 4000
    noise = 0.05

    epsilon = 2
    minPts = 3
    radius = 0.2


    # Execute experiments
    X, Y = letter()
    experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius, root_saving=root_saving)