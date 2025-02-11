import numpy as np
from prettytable import PrettyTable
from .poly_plot import plot_empir


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

    print(y_values_for_interval)

    x = np.concatenate(([first_x_value], x_values, [last_x_value]))
    y = np.concatenate(([0], y_values, [1.0]))

    table_print(intervals, y_values_for_interval)

    plot_empir(x, y, intervals, y_values_for_interval)

    return y_values_for_interval


def table_print(x_val, y_val):
    table = PrettyTable()
    table.field_names = ["x", "F*(x)"]
    for i in range(np.size(y_val)):
        if i == 0:
            table.add_row([f"x <= {x_val[i]}", y_val[i]], divider=True)
        elif i == np.size(y_val)-1:
            table.add_row([f"x > {x_val[i]}", y_val[i]], divider=True)
        else:
            table.add_row([f"{x_val[i]} < x <= {x_val[i+1]}", y_val[i]], divider=True)
    print(table)
