
from utils.datasets import shuttle
from utils.experiments import experiment

root_saving = "../visuals/experiments/shuttle/"
sizes = [5000, 10000, 15000, 20000, 25000]

epsilons = [0.5]
minPts = [20]
rs = [0.02, 0.01, 0.005, 0.001]


if __name__ == "__main__":
    results = experiment(epsilons, minPts, rs, sizes, shuttle, "results_shuttle", root_saving=root_saving)