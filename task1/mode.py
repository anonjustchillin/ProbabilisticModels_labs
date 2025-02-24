import numpy as np


def mode_dsd(values, counts):
    max_vals = []
    max_one_val = max(counts)
    indeces = np.where(counts == max_one_val)[0]

    for i in indeces:
        max_vals.append(values[i])

    #Mo = 0
    #for i in max_vals:
    #    Mo += i
    #Mo /= len(max_vals)
    #print(f"Mo* (для дискретного розподілу вибірки) = {Mo}")

    print(f"Mo* (для дискретного розподілу вибірки) = {list(map(str, max_vals))}")


def mode_isd(intervals, n_data, h):
    max_vals = []
    max_one_val = max(n_data)
    indeces = np.where(n_data == max_one_val)[0]

    for i in indeces:
        max_vals.append(intervals[i])

    first_i = indeces[0]
    x_i1 = intervals[first_i]

    mode = []
    for i in range(np.size(indeces)):
        mode.append(x_i1 + h*((max_vals[i] - n_data[indeces[i]-1]) / 
                              (2*max_vals[i] - n_data[indeces[i]-1] - n_data[indeces[i]+1])))

    print(f"Mo* (для інтегрального розподілу вибірки) = {list(map(str, max_vals))}")
