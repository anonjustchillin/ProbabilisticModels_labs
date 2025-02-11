import numpy as np
from prettytable import PrettyTable
from .poly_plot import plot_empir

table = PrettyTable()


def empir_func(values, counts, intervals, n_data, n):
    # Функціональний ряд для дискретного
    y_values = []
    sum = 0
    y_values.append(0)
    for i in range(np.size(values)-1):
        sum += counts[i]
        y_values.append(round(sum/n, 3))
    y_values.append(1)

    x_values = np.insert(values, 0, values[0] - 0.1)
    last_x_value = x_values[-1] + (x_values[-1] * 0.1)
    first_x_value = x_values[0] - 0.5

    table_print(x_values, y_values)

    # Функціональний ряд для інтервального
    y_values_for_interval = []
    y_values_for_interval.append(0)
    sum = 0
    for i in range(np.size(intervals)-1):
        sum += n_data[i]
        y_values_for_interval.append(sum / n)

    x = np.concatenate(([first_x_value], x_values, [last_x_value]))
    y = np.concatenate(([0], y_values, [1.0]))

    plot_empir(x, y, intervals, y_values_for_interval)

    return y_values_for_interval


def table_print(x_val, y_val):
    table.field_names = ["x", "F*(x)"]
    for i in range(np.size(y_val)):
        table.add_row([x_val[i], y_val[i]], divider=True)
    print(table)
