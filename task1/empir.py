import numpy as np
from prettytable import PrettyTable
from .poly_plot import plot_empir


def empir_func(values, counts, intervals, n_data, n):
    # Функціональний ряд для дискретного
    counts = np.insert(counts,0,0)
    y_values = []
    sum = 0
    # y_values.append(0)
    for i in range(np.size(counts)-1):
        sum += counts[i]
        y_values.append(round(sum/n, 6))
    y_values.append(1)

    table_print_dsd(values, y_values)

    # Функціональний ряд для інтервального
    y_values_for_interval = []
    sum = 0
    for i in range(np.size(intervals)):
        if i == 0:
            y_values_for_interval.append(0)
            continue
        sum += n_data[i-1]
        y_values_for_interval.append(sum / n)

    table_print_isd(intervals, y_values_for_interval)

    x_values = np.insert(values, 0, values[0] - 0.1)
    last_x_value = x_values[-1] + (x_values[-1] * 0.1)
    first_x_value = x_values[0] - 0.5

    x = np.concatenate(([first_x_value], x_values, [last_x_value]))
    y = np.concatenate(([0], y_values, [1.0]))

    plot_empir(x, y, intervals, y_values_for_interval)

    return y_values_for_interval


def table_print_dsd(x_val, y_val):
    table = PrettyTable()
    table.field_names = ["x", "F*(x)"]
    table.add_row([f"x <= {x_val[0]}", y_val[0]], divider=True)
    for i in range(np.size(x_val)):
        if i == np.size(x_val)-1:
            table.add_row([f"x > {x_val[i]}", y_val[i+1]], divider=True)
        else:
            table.add_row([f"{x_val[i]} < x <= {x_val[i+1]}", y_val[i+1]], divider=True)
    print(table)


def table_print_isd(x_val, y_val):
    table = PrettyTable()
    table.field_names = ["x", "F*(x)"]
    for i in range(np.size(y_val)):
        table.add_row([f"x = {x_val[i]}", y_val[i]], divider=True)
    print(table)
