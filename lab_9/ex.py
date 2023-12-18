import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

OUT = "graphs"
np.random.seed(0)

# 1)
N = 2000

# generate signal
t = np.linspace(0, 70, N)
trend = 1 / 10 * ((t - 25) ** 2) + 4 * t + 10
seasonal = 20 * np.sin(2 * np.pi * 0.5 * t) + 30 * np.sin(2 * np.pi * 0.1 * t)
noise = 30 * np.random.rand(N)
ts = trend + seasonal + noise


# 2)
def mse(x, s):
    return np.mean((x - s) ** 2)


def generate_s(x, a):
    s = np.zeros(x.shape[0])
    s[0] = x[0]
    for i in range(1, x.shape[0]):
        s[i] = a * x[i] + (1 - a) * s[i - 1]
    return s


# random prediction
s = generate_s(ts, 0.1)

fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="ts")
(l2,) = ax.plot(s, label="exp. mean")
ax.set_title(f"a=0.1, mse={np.round(mse(ts, s), 4)}")
fig.legend(handles=[l1, l2])
fig.savefig(f"{OUT}/2_random.pdf", format="pdf")

min_mse, best_a = 100000, -1
for a in range(0, 100):
    s_ = generate_s(ts, a / 100)
    mse_ = mse(ts[2:], s_[1:-1])
    if mse_ < min_mse:
        min_mse = mse_
        best_a = a / 100

# after parameter tuning
print(f"Min MSE achieved with a={best_a}")
best_s = generate_s(ts, best_a)

fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="ts")
(l2,) = ax.plot(best_s, label="exp. mean")
ax.set_title(f"a={np.round(best_a, 4)}, mse={np.round(min_mse, 4)}")
fig.legend(handles=[l1, l2])
fig.savefig(f"{OUT}/2_best.pdf", format="pdf")


# 3) MA model
def get_mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)


gaussian_noise_sz = dict()
for i in range(1, ts.shape[0] + 1):
    gaussian_noise_sz[i] = np.random.normal(size=i)


def get_ma_model(ts, q, mean):
    m = ts.shape[0]
    noise = gaussian_noise_sz[m + q]

    y = np.zeros(m)
    for i in range(m):
        y[i] = ts[m - 1 - i] - noise[-1 - i] - mean

    Y = np.zeros((m, q))
    for i in range(m):
        if -1 - 1 - i - q == -1:
            Y[i] = noise[-1 - 1 - i :: -1]
        else:
            Y[i] = noise[-1 - 1 - i : -1 - 1 - i - q : -1]

    o = np.linalg.lstsq(Y, y, rcond=None)[0]
    return o


def predict_ma(ts, m, q, mean):
    o = get_ma_model(ts[:m], q, mean)
    y_pred = ts[:m]

    N = ts.shape[0]
    noise = gaussian_noise_sz[N]

    for i in range(m, N):
        pred = mean + noise[i] + noise[i - 1 : i - q - 1 : -1] @ o
        y_pred = np.append(y_pred, pred)

    return y_pred


mean = np.mean(ts)  # we "predict" the mean of the timeseries
min_mse, best_m, best_q = None, None, None
test_cutoff = 1000
for q in range(1, 1000):
    y_pred = predict_ma(ts, test_cutoff, q, mean)
    mse = get_mse(y_pred, ts)
    if min_mse == None or mse < min_mse:
        print(f"MA mse={mse}, q={q}")
        min_mse, best_q = mse, q

y_pred = predict_ma(ts, test_cutoff, best_q, mean)
fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="actual")
(l2,) = ax.plot(y_pred, label="predicted")
ax.legend(handles=[l1, l2])
ax.set_title(f"MA q={best_q}, mse={np.round(get_mse(y_pred, ts), 4)}")
fig.savefig(f"{OUT}/3.pdf", format="pdf")

# 4) ARMA model
test_cutoff = 1200

arma = ARIMA(
    ts[:test_cutoff],
    order=([x for x in range(1, 20 + 1)], 0, [x for x in range(1, 20 + 1)]),
    trend="t",
)
arma_fit = arma.fit()
pred = arma_fit.forecast(ts.shape[0] - test_cutoff)
mse = get_mse(pred, ts[test_cutoff:])

fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="actual")
(l2,) = ax.plot(np.append(ts[:test_cutoff].copy(), pred), label="predicted")
ax.legend(handles=[l1, l2])
ax.set_title(f"ARMA mse={np.round(get_mse(pred, ts[test_cutoff:]), 4)}")
fig.savefig(f"{OUT}/4.pdf", format="pdf")
