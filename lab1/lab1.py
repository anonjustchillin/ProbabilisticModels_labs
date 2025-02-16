import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from task1.dsd import dsd_calc
from task1.isd import isd_calc
from task1.empir import empir_func
from task1.mode import mode_dsd, mode_isd
from task1.median import median_dsd, median_isd

N = 1000
n = 75

data_1 = np.array([
    42, 55, 51, 53, 58,
    41, 30, 48, 54, 46,
    50, 49, 62, 34, 35,
    62, 41, 40, 38, 34,
    63, 34, 41, 41, 46,
    48, 57, 50, 53, 54,
    31, 48, 55, 53, 60,
    58, 63, 47, 42, 65,
    53, 51, 43, 46, 57,
    44, 53, 45, 54, 46,
    52, 44, 40, 57, 45,
    37, 53, 30, 33, 59,
    50, 40, 39, 38, 45,
    55, 57, 77, 44, 40,
    46, 40, 28, 46, 43
])

data_2 = np.array([
    48, 57, 50, 53, 54,
    31, 48, 55, 53, 60,
    58, 63, 47, 42, 65,
    53, 51, 43, 46, 57,
    44, 53, 45, 54, 46,
    52, 44, 40, 57, 45,
    37, 53, 30, 33, 59,
    50, 40, 39, 38, 45,
    55, 57, 77, 44, 40,
    46, 40, 28, 46, 43,
    48, 46, 49, 55, 52,
    47, 51, 36, 47, 56,
    55, 50, 39, 43, 55,
    49, 56, 44, 55, 59,
    52, 36, 62, 49, 32
])

data_3 = np.array([
    44, 42, 60, 44, 49,
    44, 48, 52, 48, 56,
    56, 63, 58, 52, 60,
    36, 37, 42, 39, 38,
    57, 55, 66, 61, 40,
    48, 29, 52, 55, 63,
    67, 64, 44, 53, 69,
    32, 53, 44, 36, 45,
    49, 63, 53, 40, 45,
    66, 41, 43, 60, 61,
    45, 51, 58, 76, 48,
    59, 42, 62, 39, 51,
    60, 66, 71, 73, 61,
    46, 48, 50, 37, 34,
    55, 53, 42, 26, 69
])

data_4 = np.array([
    48, 54, 58, 47, 45,
    49, 45, 57, 46, 43,
    53, 49, 44, 59, 49,
    48, 47, 48, 46, 53,
    47, 51, 47, 50, 50,
    58, 52, 54, 38, 51,
    57, 44, 56, 49, 45,
    48, 47, 63, 48, 51,
    54, 44, 48, 53, 40,
    41, 53, 54, 50, 52,
    42, 50, 52, 47, 55,
    50, 48, 53, 45, 56,
    43, 54, 55, 47, 43,
    49, 48, 61, 52, 42,
    43, 45, 52, 53, 51
])

data_5 = np.array([
    48, 29, 52, 55, 63,
    67, 64, 44, 53, 69,
    32, 53, 44, 36, 45,
    49, 63, 53, 40, 45,
    66, 41, 43, 60, 61,
    59, 72, 47, 39, 39,
    54, 57, 39, 57, 49,
    57, 59, 39, 45, 33,
    70, 64, 49, 48, 62,
    52, 55, 55, 60, 46,
    44, 42, 60, 44, 58,
    44, 48, 52, 48, 56,
    56, 63, 58, 52, 60,
    36, 37, 42, 39, 38,
    57, 55, 66, 61, 40
])


def arr_analysis(data):
    var_arr = np.sort(data)
    print("Варіаційний ряд\n", var_arr)
    print()

    values, counts = np.unique(var_arr, return_counts=True)
    table = PrettyTable()
    table.field_names = ["Унікальне значення", "Кількість"]
    print()

    dsd_calc(values, counts, n)
    intervals, n_data, h = isd_calc(values, counts, n, True)
    y_values_for_interval = empir_func(values, counts, intervals, n_data, n)

    mode_dsd(values, counts)
    median_dsd(values)

    mode_isd(intervals, n_data, h)
    median_isd(y_values_for_interval, intervals, h)

    R = max(values) - min(values)
    print(f"R = {R}")

    av_value = round(np.sum(values * counts) / n, 6)
    print(f"x_B = {av_value}")

    d = round(np.sum(np.power(values, 2) * counts) / n - np.power(av_value, 2), 6)
    print(f"D_b = {d}")

    sigma = round(np.sqrt(d), 6)
    print(f"sigma = {sigma}")

    coef_variation = round(sigma / av_value * 100, 6)
    print(f"V = {coef_variation}%")

    return av_value


def control_map_plt(x_B1, x_B2, x_B3, x_B4, x_B5):
    x_B = [x_B1, x_B2, x_B3, x_B4, x_B5]
    T_nom = 50
    sigma = 2.5

    for x in x_B:
        if x > (T_nom + 2*sigma/np.sqrt(n)) or x < (T_nom - 2*sigma/np.sqrt(n)):
            print("Результат вимірювання не відповідає умовам замовника :(")
        else:
            print("Результат вимірювання відповідає умовам замовника :)")

    plt.plot(x_B, marker='o', linestyle='-', color='red')
    plt.axhline(y=T_nom, color='green', linestyle='--', label='Середнє')
    plt.axhline(y=T_nom + 2 * sigma / np.sqrt(n), color='y', linestyle='--', label='+2σ')
    plt.axhline(y=T_nom - 2 * sigma / np.sqrt(n), color='y', linestyle='--', label='-2σ')
    plt.axhline(y=T_nom + 3 * sigma / np.sqrt(n), color='b', linestyle='--', label='+3σ')
    plt.axhline(y=T_nom - 3 * sigma / np.sqrt(n), color='b', linestyle='--', label='-3σ')
    plt.legend()

    plt.xlabel('Номер вибірки')
    plt.title('Контрольна карта середнії арифметичних')
    plt.show()


def start():
    print("-------------------- ВИБІРКА 1 --------------------")
    x_B1 = arr_analysis(data_1)
    print()
    print("-------------------- ВИБІРКА 2 --------------------")
    x_B2 = arr_analysis(data_2)
    print()
    print("-------------------- ВИБІРКА 3 --------------------")
    x_B3 = arr_analysis(data_3)
    print()
    print(" --------------------ВИБІРКА 4 --------------------")
    x_B4 = arr_analysis(data_4)
    print()
    print(" --------------------ВИБІРКА 5 --------------------")
    x_B5 = arr_analysis(data_5)
    print()

    control_map_plt(x_B1, x_B2, x_B3, x_B4, x_B5)
