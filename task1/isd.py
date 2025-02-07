import numpy as np
from prettytable import PrettyTable

table = PrettyTable()


def check(x, num1, num2):
    return (x > num1 and x < num2)


def isd_calc(values, counts, n):
    check_last_val = True

    k = round(np.sqrt(n))
    print(k)
    h = round((max(values) - min(values))/k, 3)
    print(h)

    data = np.array([round((values[0] + i * h), 2) for i in range(k+1)])
    if data[-1] < values[-1]:
        check_last_val = False
    print(data)

    n_data = np.array([])
    num = 0
    saved = 0
    flag = 0
    count = 0
    
    for i in range(np.size(data)-1):
        for j in range(flag, np.size(values)):
            if check(values[j], data[i], data[i+1]) or j == 0 or j == np.size(values)-1:
                num += counts[j]
                continue
            elif values[j] == data[i] or values[j] == data[i+1]:
                j1 = round(counts[j]/2)
                j2 = counts[j] - j1
                saved = max(j1, j2)
                num += min(j1, j2)
                flag = j+1
            else:
                flag = j
            break
        n_data = np.append(n_data, num)
        num *= 0
        num += saved
        saved *= 0
    print(n_data)

    w_div_h = []
    for i in n_data:
        w_div_h.append(round(i/(n*h), 3))

    table_print(data, n_data, w_div_h, check_last_val)
    #plot(values, w)


def table_print(values, counts, w, check_last_val):
    table.field_names = ["Інтервали", "n*_i", "w*_i / h"]
    for i in range(np.size(counts-1)):
        if i == 0:
            table.add_row([f"[{values[i]}; {values[i+1]})", counts[i], w[i]], divider=True)
        elif i == np.size(counts-2):
            table.add_row([f"[{values[i]}; {values[i+1]}{']' if check_last_val else ')'}", counts[i], w[i]],
                          divider=True)
            break
        else:
            table.add_row([f"({values[i]}; {values[i+1]})", counts[i], w[i]], divider=True)
    print(table)
