import numpy as np
import matplotlib.pyplot as plt

OUT = "graphs"


# 1)
N = 1000

# generate signal
t = np.linspace(0, 50, N)
trend = 1 / 5 * ((t - 25) ** 2) + 4 * t + 10
seasonal = 20 * np.sin(2 * np.pi * 0.5 * t) + 30 * np.sin(2 * np.pi * 0.1 * t)
noise = 10 * np.random.rand(N)
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


s = generate_s(ts, 0.1)

fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="ts")
(l2,) = ax.plot(s, label="exp. mean")
fig.legend(handles=[l1, l2])
fig.savefig(f"{OUT}/2_0.1.pdf", format="pdf")

min_mse, best_a = 100, -1
for a in range(0, 100):
    s_ = generate_s(ts, a / 100)
    mse_ = mse(ts, s_)
    if mse_ < min_mse:
        min_mse = mse_
        best_a = a / 100

print(f"Min MSE achieved with a={best_a}")
best_s = generate_s(ts, best_a)
fig, ax = plt.subplots()
(l1,) = ax.plot(ts, label="ts")
(l2,) = ax.plot(best_s, label="exp. mean")
fig.legend(handles=[l1, l2])
fig.savefig(f"{OUT}/2_{np.round(best_a)}.pdf", format="pdf")
