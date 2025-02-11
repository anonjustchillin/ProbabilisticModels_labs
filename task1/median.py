import numpy as np
import statistics as st


def median_dsd(values):
    print(f"Me* (для дискретного розподілу вибірки) = {st.median(values)}")


def median_isd(empir, intervals, h):
    median = 0
    for i in range(np.size(empir)):
        if empir[i] < 0.5 < empir[i + 1]:
            median = (intervals[i] + (h * (0.5 - empir[i]) /
                      (empir[i + 1] - empir[i])))
            break

    print(f"Me* (для інтегрального розподілу вибірки) = {round(median, 3)}")
