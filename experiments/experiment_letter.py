
from utils.datasets import letter
from utils.experiments import experiment

root_saving = "../visuals/experiments/letter/"

sizes = [2000, 4000, 6000, 8000]
minPts = [8, 16, 24, 32]

epsilons = [0.5]
rs = [0.4, 0.35, 0.3, 0.25]


if __name__ == "__main__":
    experiment(epsilons, minPts, rs, sizes, letter,
               name_experiment="scratch_results_letter", sklearn=False, root_saving=root_saving)
    #experiment(epsilons, minPts, rs, sizes, letter,
    #           name_experiment="sklearn_results_letter", sklearn=True, root_saving=root_saving)