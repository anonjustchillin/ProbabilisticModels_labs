import numpy as np
from prettytable import PrettyTable
from .dsd import dsd_calc
from .isd import isd_calc
from .empir import empir_func
from .mode import mode_dsd, mode_isd
from .median import median_dsd, median_isd


# variant 22nd
# data = np.array([12, 15, 7, 19, 15, 27, 22, 4,
#                  11, 19, 15, 7, 1, 12, 22, 4,
#                  11, 15, 19, 12, 7, 27, 15, 19,
#                  11, 22, 12, 19, 15, 12, 15, 31])

# data = np.array([0.87, 0.94, 0.99, 0.90, 0.90, 0.87, 0.85, 0.87,
#                      0.90, 0.94, 0.87, 0.87, 0.82, 0.90, 0.94, 0.90,
#                      0.85, 0.85, 0.87, 0.94, 0.81, 0.82, 0.87, 0.97,
#                      0.90, 0.94, 0.85, 0.81, 0.87, 0.85, 0.90, 0.82,
#                      0.99, 0.90, 0.94, 0.82, 0.97, 0.81, 0.85, 0.87])

data = np.array([2, 0, 1, 1.5, 5, 3, 0, 1, 2.2, 1.7,
                 0.5, 4, 0.2, 0, 1.2, 0, 2.2, 2.8, 0, 3.2,
                 0.7, 0, 2.1, 1.7, 3.2, 5, 1.2, 0.4, 0.3, 2,
                 0.8, 0.3, 0, 0, 0.5, 0.4, 0.2, 0.7, 1.2, 0.4,
                 1.5, 0.4, 0.5, 0.3, 0.8, 1, 0.4, 3, 2.1, 0.5])


var_arr = np.sort(data)
n = np.size(data)


def start():
    values, counts = np.unique(var_arr, return_counts=True)
    table = PrettyTable()
    table.field_names = ["Унікальне значення", "Кількість"]
    for i in range(np.size(values)):
        table.add_row([values[i], counts[i]], divider=True)
    print(table)

    dsd_calc(values, counts, n)
    intervals, n_data, h = isd_calc(values, counts, n)
    y_values_for_interval = empir_func(values, counts, intervals, n_data, n)
    mode_dsd(values, counts)
    median_dsd(values)
    mode_isd(intervals, n_data, h)
    median_isd(y_values_for_interval, intervals, h)

