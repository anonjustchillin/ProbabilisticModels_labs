import numpy as np
from .dsd import dsd_calc
from .isd import isd_calc
from .empir import empir_func


# variant 22nd
data = np.array([12, 15, 7, 19, 15, 27, 22, 4,
                 11, 19, 15, 7, 1, 12, 22, 4,
                 11, 15, 19, 12, 7, 27, 15, 19,
                 11, 22, 12, 19, 15, 12, 15, 31])

# data = np.array([0.87, 0.94, 0.99, 0.90, 0.90, 0.87, 0.85, 0.87,
#                   0.90, 0.94, 0.87, 0.87, 0.82, 0.90, 0.94, 0.90,
#                   0.85, 0.85, 0.87, 0.94, 0.81, 0.82, 0.87, 0.97,
#                   0.90, 0.94, 0.85, 0.81, 0.87, 0.85, 0.90, 0.82,
#                   0.99, 0.90, 0.94, 0.82, 0.97, 0.81, 0.85, 0.87])

var_arr = np.sort(data)
n = np.size(data)


def start():
    values, counts = np.unique(var_arr, return_counts=True)

    w = []
    for i in counts:
        w.append(i/n)

    dsd_calc(values, counts, w)
    data, n_data = isd_calc(values, counts, n)
    empir_func(values, w, data, n_data, n)

