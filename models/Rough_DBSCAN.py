
from sklearn.cluster import DBSCAN
from models.Counted_Leaders import Counted_Leaders


class Rough_DBSCAN:
    def __init__(self, epsilon, minPts, radius):
        self.e = epsilon
        self.minPts = minPts

        # Prepare counted leaders
        self.lstar = Counted_Leaders(X, radius)
        self.leaders = None # Extract from lstar

    def fit(self, X):
        pass

    def predict(self):
        pass

    def fit_predict(self, X):
        pass




from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("######## Starting Test ########\n")
    print("Generating dataset...")
    X, Y = make_moons(n_samples=4000, noise=0.1, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], c=Y)
    plt.title("Banana dataset")
    #plt.show()

    print("\nStarting Classification...")
    rdbscan = Rough_DBSCAN(0.1, 4, 8)



