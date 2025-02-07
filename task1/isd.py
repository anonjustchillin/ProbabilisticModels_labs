import numpy as np
from prettytable import PrettyTable
from .poly_plot import plot

table = PrettyTable()


def isd_calc(values, counts, n):
    check_last_val = True

    k = round(np.sqrt(n))
    print(k)
    h = (max(values) - min(values))/k
    print(h)

    data = np.array([])
    count = 0
    curr_value = round(values[0], 2)
    while count < k:
        np.append(data, round(curr_value, 2))
        count += 1
        curr_value += h

    if (curr_value+h) < values[np.size(values)-1]:
        check_last_val = False
    print(data)

    n_data = np.array([])
    num = 0
    saved = 0
    flag = 0
    for i in range(len(data)-1):
        for j in range(flag, np.size(counts)-1):
            if counts[j] > data[i] and counts[j] < data[i+1]:
                num += counts[j]
                continue
            else:
                j1 = round(counts[j]/2)
                j2 = counts[j] - j1
                if j1 < j2:
                    num += j1
                    saved = j2
                else:
                    num += j2
                    saved = j1
            np.append(n_data, num)
            num = saved
            saved *= 0
            flag = j
    print(n_data)

    w_div_h = []
    for i in n_data:
        w_div_h.append(i/(n*h))
    
    cols = round(len(data)/2)
    data2d = data.reshape(cols, 2)

    table_print(data2d, n_data, w_div_h, check_last_val)
    #plot(values, w)


def table_print(values, counts, w, check_last_val):
    table.field_names = ["Інтервали", "n*_i", "w*_i / h"]
    for i in range(np.size(counts)):
        if i == 0:
            table.add_row([f"[{values[i][0]}; {values[i][1]})", counts[i], w[i]], divider=True)
        elif i == np.size(values)-1:
            table.add_row([f"[{values[i][0]}; {values[i][1]}{']' if check_last_val else ')'}", counts[i], w[i]],
                          divider=True)
        else:
            table.add_row([f"({values[i][0]}; {values[i][1]})", counts[i], w[i]], divider=True)
    print(table)
