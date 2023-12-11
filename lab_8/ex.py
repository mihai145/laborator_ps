import numpy as np
import matplotlib.pyplot as plt

OUT = "graphs"


# a)
N = 1000

# generate signal
t = np.linspace(0, 50, N)
trend = 1 / 5 * ((t - 25) ** 2) + 4 * t + 10
seasonal = 20 * np.sin(2 * np.pi * 0.5 * t) + 30 * np.sin(2 * np.pi * 0.1 * t)
noise = 10 * np.random.rand(N)
ts = trend + seasonal + noise

fig, axs = plt.subplots(4, 1, figsize=(12, 10))
fig.tight_layout(pad=1.5)
axs[0].plot(ts)
axs[0].set_title("Timeseries")
axs[1].plot(trend)
axs[1].set_title("Trend")
axs[2].plot(seasonal)
axs[2].set_title("Seasonal")
axs[3].plot(noise)
axs[3].set_title("Noise")
fig.savefig(f"{OUT}/1a.pdf", format="pdf")

# b)
# remove mean from all elements
ts_ = ts - np.mean(ts)

# compute auto correlation
auto_correlation = np.correlate(ts_, ts_, mode="full").astype(dtype=np.float64)

# divide by norm
auto_correlation /= np.sum(np.array([x**2 for x in ts_]))

# result is mirrored - keep one half
auto_correlation = auto_correlation[len(auto_correlation) // 2 :]

fig, ax = plt.subplots()
ax.plot(auto_correlation)
ax.set_title("Auto correlation")
fig.savefig(f"{OUT}/1b.pdf", format="pdf")


# c)
def get_mse(y_pred, y):
    return np.mean((y_pred - y) ** 2)


def get_Y(arr, m, p):
    Y = np.zeros((m, p))
    for i in range(m):
        if i > 0:
            Y[i] = arr[p - 1 + i : -1 + i : -1]
        else:
            Y[0] = arr[p - 1 :: -1]

    return Y


def least_squares(arr, p):
    m = len(arr) - p
    Y = get_Y(arr, m, p)
    b = arr[p:]

    return np.linalg.lstsq(Y, b, rcond=None)[0]


def get_predictions(arr, m, p):
    y_pred = []
    for i in range(m + p - 1, N - 1):
        coefs = least_squares(arr[i - m - p + 1 : i + 1], p)

        Y = get_Y(arr[i - m - p + 2 : i + 2], m, p)
        y = Y @ coefs

        y_pred.append(y[-1])

    return y_pred


def draw_predictions(arr, m, p, out_path):
    y_pred = get_predictions(arr, m, p)
    y_pred = np.concatenate((arr[: m + p], y_pred), axis=0)

    mse = get_mse(y_pred, ts)

    fig, ax = plt.subplots()
    (l1,) = ax.plot(arr, label="Actual")
    (l2,) = ax.plot(y_pred, label="Predicted")
    ax.legend(handles=[l1, l2])
    ax.set_title(f"AR with m={m}, p={p}, mse={np.round(mse, 4)}")
    fig.savefig(out_path, format="pdf")


draw_predictions(ts, 10, 5, f"{OUT}/1c.pdf")


# d)
min_mse, coefs = 100, (-1, -1)
for m in range(1, 50 + 1):
    for p in range(1, 50 + 1):
        y_pred = get_predictions(ts, m, p)
        y_pred = np.concatenate((ts[: m + p], y_pred), axis=0)

        mse = get_mse(y_pred, ts)
        if min_mse > mse:
            min_mse = mse
            coefs = (m, p)

print(f"Min mse {min_mse}, achieved with m={m}, p={p}")
draw_predictions(ts, coefs[0], coefs[1], f"{OUT}/1d.pdf")
