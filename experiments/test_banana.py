
from utils.datasets import banana
from utils.experiments import experiment

root_saving = "../visuals/banana/"


if __name__ == "__main__":

    # Hyperparameters
    n_samples = 4000
    noise = 0.05

    epsilon = 0.2
    minPts = 8
    radius = 0.1

    
    # Execute experiments
    X, Y = banana(n_samples=n_samples, noise=noise, random_state=0)
    experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius, root_saving=root_saving)