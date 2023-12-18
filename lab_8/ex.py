import numpy as np
import matplotlib.pyplot as plt

OUT = "graphs"
np.random.seed(145)

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


# ts - vector of size m+p
def get_ar_model(ts, m, p):
    if ts.shape[0] != m + p:
        raise ValueError(f"The input has size {ts.shape[0]}, expected {m+p}")

    y = ts[-1 : -m - 1 : -1]

    Y = np.zeros((m, p))
    for i in range(m):
        Y[i] = ts[-1 - 1 - i : -1 - 1 - p - i : -1]

    x = np.linalg.lstsq(Y, y, rcond=None)[0]
    return x


def get_predictions(ts, m, p):
    x = get_ar_model(ts[: m + p], m, p)
    y_pred = ts[: m + p].copy()
    n = ts.shape[0]

    for i in range(m + p, n):
        if i - p - 1 == -1:
            pred = y_pred[i - 1 :: -1] @ x
        else:
            pred = y_pred[i - 1 : i - p - 1 : -1] @ x
        y_pred = np.append(y_pred, pred)

    return y_pred


y_pred = get_predictions(ts, 237, 124)

fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="actual")
(l2,) = ax.plot(y_pred, label="predicted")
ax.legend(handles=[l1, l2])
ax.set_title(f"m=237, p=124, mse={np.round(get_mse(y_pred, ts), 4)}")
fig.savefig(f"{OUT}/1c.pdf", format="pdf")


# d)
# Tune m and p
best_mse, best_m, best_p = None, None, None
for m in range(1, 300):
    for p in range(1, m - 1):
        y_pred = get_predictions(ts, m, p)
        mse = get_mse(y_pred, ts)

        if best_mse is None or mse < best_mse:
            print(f"Mse: {mse}, m: {m}, p: {p}")
            best_mse, best_m, best_p = mse, m, p

y_pred = get_predictions(ts, best_m, best_p)

fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="actual")
(l2,) = ax.plot(y_pred, label="predicted")
ax.legend(handles=[l1, l2])
ax.set_title(f"m={best_m}, p={best_p}, mse={np.round(get_mse(y_pred, ts), 4)}")
fig.savefig(f"{OUT}/1d.pdf", format="pdf")
