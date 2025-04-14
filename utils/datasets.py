
from sklearn.datasets import make_moons
from sklearn.datasets import make_blobs


def banana(n_samples, noise, random_state=0, verbose=True):
    if verbose:
        print("\n-------- Starting Test --------\n")
        print("Generating BANANA dataset")
    return make_moons(n_samples=n_samples, noise=noise, random_state=random_state)


def blobs(n_samples, centers, cluster_std, random_state=0, verbose=True):
    if verbose:
        print("\n-------- Starting Test --------\n")
        print("Generating BLOBS dataset")
    return make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=random_state)


def letter(verbose=True):
    if verbose:
        print("\n-------- Starting Test --------\n")
        print("Loading LETTER dataset")
    pass


def pendigits(verbose=True):
    if verbose:
        print("\n-------- Starting Test --------\n")
        print("Loading PENDIGITS dataset")
    pass


def shuttle(verbose=True):
    if verbose:
        print("\n-------- Starting Test --------\n")
        print("Loading SHUTTLE dataset")
    pass