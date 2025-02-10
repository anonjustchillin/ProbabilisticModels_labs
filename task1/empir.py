import numpy as np
from .poly_plot import plot_empir


def empir_func(x_i, w_i,  intervals, n_i, n):
    # Функціональний ряд для дискретного
    w_i = np.insert(w_i, 0, 0)
    y_values = []
    sum = 0
    for i in range(len(x_i)):
        sum += w_i[i]
        y_values.append(round(sum,3))
    y_values.append(1)

    x_values = np.insert(x_i, 0, x_i[0] - 0.1)
    last_x_value = x_values[-1] + (x_values[-1] * 0.1)
    first_x_value = x_values[0] - 0.5
    x = np.concatenate(([first_x_value], x_values, [last_x_value]))
    y = np.concatenate(([0], y_values, [1.0]))

    # Функціональний ряд для інтервального
    y_values_for_interval = []
    sum_for_interval = 0
    for i in range(len(intervals)):
        if i == 0:
            y_values_for_interval.append(0)
        else:
            sum_for_interval += n_i[i-1]
            y_values_for_interval.append(sum_for_interval / n)

    plot_empir(x, y, intervals, y_values_for_interval)
