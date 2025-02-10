import numpy as np
import statistics as st


def mode_dsd(values):
    mode = st.mode(values)
    print(f"Mo* (для дискретного розподілу вибірки) = {mode}")


def mode_isd(intervals, n_data, h):
    max_val = max(n_data)
    indeces = np.where(n_data == max_val)[0]

    n_Mo = 0
    for i in indeces:
        n_Mo += n_data[i]

    first_i = indeces[0]
    x_i1 = intervals[first_i]

    mode = x_i1 + h*((max_val - n_data[first_i-1]) / (2*max_val - n_data[first_i-1] - n_data[first_i+1]))
    print(f"Mo* (для інтегрального розподілу вибірки) = {round(mode, 3)}")
