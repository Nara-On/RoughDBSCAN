
from utils.datasets import blobs, banana, letter, pendigits, shuttle
from utils.experiments import experiment_counted_leaders
from utils.plots import plot_leader_count

root_saving = "../visuals/experiments/leaders/new/"

parameters = [
    ("Banana", banana, [1000, 2000, 3000, 4000, 5000], [0.1, 0.25, 0.5, 0.75]),
    ("Blobs", blobs, [3000, 6000, 9000, 12000, 15000], [0.2, 0.4, 0.6, 0.8]),
    ("Letter", letter, [2000, 4000, 6000, 8000, 10000], [0.4, 0.35, 0.3, 0.25]),
    ("PenDigits", pendigits, [1000, 2000, 4000, 6000, 8000], [30, 25, 20, 15]),
    ("Shuttle", shuttle, [5000, 10000, 15000, 20000, 25000], [0.02, 0.01, 0.005, 0.001]),
]


if __name__ == "__main__":
    results = experiment_counted_leaders(parameters, root_saving=root_saving)

    plot_leader_count(results, root_saving + "results_leaders_patterns.jpg",
                      figsize_w=18, figsize_h=15)

    best = results["Name"].isin(["Banana", "Blobs", "PenDigits", "Letter"])
    plot_leader_count(results[best], root_saving + "results_leaders_patterns_best_4.jpg",
                      figsize_w=15, figsize_h=10)

    worst = results["Name"].isin(["Letter", "Shuttle"])
    plot_leader_count(results[worst], root_saving + "results_leaders_patterns_worst_2.jpg",
                      figsize_w=12, figsize_h=5)
