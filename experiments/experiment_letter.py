
from utils.datasets import letter
from utils.experiments import experiment

root_saving = "../visuals/experiments/letter/"
sizes = [2000, 4000, 6000, 8000, 10000]

epsilons = [0.5]
minPts = [8]
rs = [0.4, 0.35, 0.3, 0.25]


if __name__ == "__main__":
    results = experiment(epsilons, minPts, rs, sizes, letter, "results_letter", root_saving=root_saving)