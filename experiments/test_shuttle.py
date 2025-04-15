
from utils.datasets import shuttle
from utils.experiments import experiment

root_saving = "../visuals/shuttle/"


if __name__ == "__main__":

    # Hyperparameters
    size = 5000

    epsilon = 0.03
    minPts = 20
    radius = 0.001


    # Execute experiments
    X, Y = shuttle(size)
    experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
               name_experiment=f"{size}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving)