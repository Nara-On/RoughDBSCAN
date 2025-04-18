
from utils.datasets import shuttle
from utils.experiments import experiment

root_saving = "../visuals/experiments/shuttle/"

sizes = [5000, 10000, 15000, 20000]
minPts = [20, 40, 60, 80]

epsilons = [0.5]
rs = [0.02, 0.01, 0.005, 0.001]


if __name__ == "__main__":
    experiment(epsilons, minPts, rs, sizes, shuttle,
               name_experiment="scratch_results_shuttle", sklearn=False, root_saving=root_saving)
    #experiment(epsilons, minPts, rs, sizes, shuttle,
    #           name_experiment="sklearn_results_shuttle", sklearn=True, root_saving=root_saving)