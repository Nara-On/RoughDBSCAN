
from sklearn.datasets import make_moons
from sklearn.datasets import make_blobs

import numpy as np
import pandas as pd


def banana(n_samples, noise=0.05, random_state=0, verbose=True):
    if verbose:
        print(f"Generating {n_samples} samples from BANANA dataset")
    return make_moons(n_samples=n_samples, noise=noise, random_state=random_state)


def blobs(n_samples, centers=3, cluster_std=0.5, random_state=0, verbose=True):
    if verbose:
        print(f"Generating {n_samples} samples from BLOBS dataset")
    return make_blobs(n_samples=n_samples, centers=int(centers), cluster_std=cluster_std, random_state=random_state)


def letter(size, verbose=True):
    if verbose:
        print(f"Loading {size} samples from LETTER dataset")

    data = np.loadtxt("../datasets/Letter/letter-recognition.data", dtype='float32', delimiter=',',
                      converters={0: lambda ch: ord(ch) - ord('A')})

    Y, X = np.hsplit(data[:size, :], [1])
    return X, Y.reshape((Y.shape[0],))


def pendigits(size, verbose=True):
    if verbose:
        print(f"Loading {size} samples from PENDIGITS dataset")

    data = pd.read_csv("../datasets/Pendigits/pendigits_txt.csv", delimiter=',')
    X, Y = data.iloc[:size, :-1], data.iloc[:size, -1]

    return X.to_numpy(), Y.to_numpy()


def shuttle(size, verbose=True):
    if verbose:
        print(f"Loading {size} samples from SHUTTLE dataset")

    train = pd.read_csv("../datasets/Shuttle/shuttle.trn", delimiter=' ', header=None)
    test = pd.read_csv("../datasets/Shuttle/shuttle.tst", delimiter=' ', header=None)

    data = pd.concat([train, test])
    X, Y = data.iloc[:size, :-1], data.iloc[:size, -1]

    return X.to_numpy(), Y.to_numpy()
