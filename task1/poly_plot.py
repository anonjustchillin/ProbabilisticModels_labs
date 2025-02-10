import matplotlib.pyplot as plt
import numpy as np


def plot_dsd(values, w):
    fig, ax = plt.subplots()

    ax.plot(values, w)
    ax.scatter(values, w),
    ax.set_title("Графік відносних частот")
    ax.set_xlabel("x_i")
    ax.set_ylabel("w")
    plt.show()


def plot_isd(values, w_div_h):
    bin_widths = np.diff(values)
    plt.bar(values[:-1], w_div_h, width=bin_widths, align='edge', color='darkblue', edgecolor='black')

    plt.title('Гістограма')
    plt.xlabel('$x_i$')
    plt.ylabel('$w_i$h')
    plt.grid(True)
    plt.show()


def plot_empir(x, y, intervals, y_values_for_interval):
    plt.step(x, y, where='post', label='F*(x)', color='darkblue')

    plt.title('Графік емпіричної функції')
    plt.xlabel('x')
    plt.ylabel('F*(x)')
    plt.grid(True)
    plt.legend()

    plt.plot(intervals, y_values_for_interval,linestyle='--',)
    plt.scatter(intervals, y_values_for_interval)
    plt.show()