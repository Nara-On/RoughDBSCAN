
import numpy as np

def coincidence(main, search):
    # When there are many such leaders then choose the first one according to the ordering in which the set L is created.
    #return next(i for i in main if i in set(search))
    for m in main:
        for s in search:
            if np.array_equal(m, s):
                return s