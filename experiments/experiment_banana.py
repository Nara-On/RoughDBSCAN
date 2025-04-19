
from utils.datasets import banana
from utils.experiments import experiment

root_saving = "../visuals/experiments/banana/new_"

sizes = [1000, 2000, 3000, 4000]
minPts = [2, 4, 6, 8]

epsilons = [0.2]
rs = [0.1, 0.25, 0.5, 0.75]


if __name__ == "__main__":
    experiment(epsilons, minPts, rs, sizes, banana,
               name_experiment="scratch_results_banana", sklearn=False, root_saving=root_saving)
    experiment(epsilons, minPts, rs, sizes, banana,
               name_experiment="sklearn_results_banana", sklearn=True, root_saving=root_saving)