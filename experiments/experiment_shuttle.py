
from utils.datasets import shuttle
from utils.experiments import experiment

root_saving = "../visuals/shuttle/"

e = 0.5
minPts = 20
t = [0.02, 0.01, 0.005, 0.001]

sizes = [5000, 10000, 15000, 20000, 25000]


if __name__ == "__main__":

    # Hyperparameters
    plots = True


    # Execute experiments
    #X, Y = shuttle(size)
    #experiment(X=X, Y=Y, epsilon=epsilon, minPts=minPts, radius=radius,
    #           name_experiment=f"{size}_E{epsilon}_T{minPts}_R{radius}", root_saving=root_saving, plots=plots)