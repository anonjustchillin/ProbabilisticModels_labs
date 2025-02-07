import matplotlib.pyplot as plt


def plot(values, w):
    fig, ax = plt.subplots()

    ax.plot(values, w)
    ax.scatter(values, w),
    ax.set_title("Графік відносних частот")
    ax.set_xlabel("x_i")
    ax.set_ylabel("w")
    plt.show()