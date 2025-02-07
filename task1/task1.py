import numpy as np
from .dsd import dsd_calc
from .isd import isd_calc


# variant 32nd
data = np.array([12, 15, 7, 19, 15, 27, 22, 4,
                 11, 19, 15, 7, 1, 12, 22, 4,
                 11, 15, 19, 12, 7, 27, 15, 19,
                 11, 22, 12, 19, 15, 12, 15, 31])
var_arr = np.sort(data)
n = 32


def start():
    values, counts = np.unique(data, return_counts=True)

    w = []
    for i in values:
        w.append(i/n)

    # dsd_calc(values, counts, w)
    isd_calc(values, counts, n)
