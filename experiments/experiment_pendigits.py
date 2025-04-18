
from utils.datasets import pendigits
from utils.experiments import experiment

root_saving = "../visuals/experiments/pendigits/"

sizes = [1000, 2000, 4000, 6000, 8000]
minPts = [4, 8, 16, 24, 32]

epsilons = [40]
rs = [30, 25, 20, 15]


if __name__ == "__main__":
    results = experiment(epsilons, minPts, rs, sizes, pendigits, "results_pendigits", root_saving=root_saving)