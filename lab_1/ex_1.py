import numpy as np
import matplotlib.pyplot as plt
out = "graphs"

# a)
x = np.arange(0, 0.03, 0.0005)
plt.stem(x, np.zeros(len(x)))
plt.title('Axa reala')
plt.savefig(f'{out}/ex_1_a.pdf')
plt.close()

# b)
def generate_x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)

def generate_y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)

def generate_z(t):
    return np.cos(120 * np.pi * t + np.pi / 3)

def plot_range_samples(generate_f, low, high, num_samples):
    t = np.linspace(low, high, num_samples)
    return (t, generate_f(t))

signals = [
    ('x', generate_x, 0, 0.1, 1000),    # get more samples of x(t), since it's frequency is higher
    ('y', generate_y, 0, 0.1, 500),
    ('z', generate_z, 0, 0.1, 500),
]

fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)
for i, (c, func, low, high, num_samples) in enumerate(signals):
    t, f = plot_range_samples(func, low, high, num_samples)
    axs[i].set_title(c)
    axs[i].set(ylabel=c+'(t)')
    axs[i].plot(t, f)

fig.savefig(f'{out}/ex_1_b.pdf')

# c)
def get_cnt_samples(timespan, frequency):
    return int(frequency * timespan)

# esantionare cu frecventa de 200Hz, respectiv 1000Hz
for frequency in [200, 1000]:
    sampled_signals = [
        ('x', generate_x, 0, 0.1, get_cnt_samples(0.1, frequency)),
        ('y', generate_y, 0, 0.1, get_cnt_samples(0.1, frequency)),
        ('z', generate_z, 0, 0.1, get_cnt_samples(0.1, frequency)),
    ]

    fig, axs = plt.subplots(3)
    fig.tight_layout(pad=1.5)
    for i, (tup_signal, tup_sampled_signal) in enumerate(zip(signals, sampled_signals)):
        c, func, low, high, num_samples = tup_signal
        t, f = plot_range_samples(func, low, high, num_samples)
        axs[i].set_title(c + f'(t) sampled at {frequency}hz')
        axs[i].set(ylabel=c+'(t)')
        axs[i].plot(t, f)

        c, func, low, high, num_samples = tup_sampled_signal
        t, f = plot_range_samples(func, low, high, num_samples)
        axs[i].stem(t, f)

    fig.savefig(f'{out}/ex_1_c_{frequency}hz.pdf')
