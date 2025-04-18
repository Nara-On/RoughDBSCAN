
from utils.datasets import pendigits
from utils.experiments import experiment

root_saving = "../visuals/experiments/pendigits/new_"

sizes = [1000, 2000, 4000, 6000]
minPts = [4, 8, 16, 24]

epsilons = [40]
rs = [30, 25, 20, 15]


if __name__ == "__main__":
    experiment(epsilons, minPts, rs, sizes, pendigits,
               name_experiment="scratch_results_pendigits", sklearn=False, root_saving=root_saving)
    experiment(epsilons, minPts, rs, sizes, pendigits,
               name_experiment="sklearn_results_pendigits", sklearn=True, root_saving=root_saving)
