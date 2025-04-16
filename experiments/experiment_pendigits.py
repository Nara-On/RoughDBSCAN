
from utils.datasets import pendigits
from utils.experiments import experiment

root_saving = "../visuals/pendigits/"

e = 40
minPts = 20
t = [30, 25, 20, 15]

sizes = [1000, 2000, 4000, 6000, 8000]


if __name__ == "__main__":

    # Hyperparameters
    size = 1000


    # Execute experiments
    #X, Y = pendigits(size)
    #experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
    #           name_experiment=f"{size}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=plots)