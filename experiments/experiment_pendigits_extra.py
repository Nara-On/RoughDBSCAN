
from utils.datasets import pendigits
from utils.experiments import experiment_extra

root_saving = "../visuals/experiments/pendigits/extra/"

sizes = [6000]
minPts = [24]

epsilons = [40]
rs = [30]


if __name__ == "__main__":
    experiment_extra(epsilons, minPts, rs, sizes, pendigits,
               name_experiment="scratch_results_pendigits", sklearn=False, root_saving=root_saving)
