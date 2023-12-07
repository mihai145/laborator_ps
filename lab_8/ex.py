import numpy as np
import matplotlib.pyplot as plt

OUT = "graphs"


# a)
N = 1000

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
auto_correlation = np.correlate(ts, ts, mode="full")
auto_correlation = auto_correlation[len(auto_correlation) // 2 :]

fig, ax = plt.subplots()
ax.plot(auto_correlation)
ax.set_title("Auto correlation")

fig.savefig(f"{OUT}/1b.pdf", format="pdf")

# c)


# d)
