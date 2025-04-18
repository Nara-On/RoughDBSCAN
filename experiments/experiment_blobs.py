
from utils.datasets import blobs
from utils.experiments import experiment

root_saving = "../visuals/experiments/blobs/"

sizes = [1000, 3000, 6000, 9000]
minPts = [30, 90, 180, 270]

epsilons = [0.5]
rs = [0.1, 0.25, 0.5, 0.75]


if __name__ == "__main__":
    experiment(epsilons, minPts, rs, sizes, blobs,
               name_experiment="scratch_results_blobs", sklearn=False, root_saving=root_saving)
    #experiment(epsilons, minPts, rs, sizes, blobs,
    #           name_experiment="sklearn_results_blobs", sklearn=True, root_saving=root_saving)