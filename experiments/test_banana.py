
from utils.datasets import banana
from utils.experiments import experiment

root_saving = "../visuals/banana/"


if __name__ == "__main__":

    # Hyperparameters
    n_samples = 500
    noise = 0.05

    epsilon = 0.2
    minPts = 8
    radius = 0.5

    plots = True

    
    # Execute experiments
    X, Y = banana(n_samples=n_samples, noise=noise, random_state=0)
    experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
               name_experiment=f"{n_samples}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=plots)