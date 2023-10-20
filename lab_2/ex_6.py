import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'


# Lab 1 2a)
def sine_signal_generator(freq):
    def generate_f(t):
        return np.sin(freq * 2 * np.pi * t)
    return generate_f

sample_frequency = 10
timespan = 10
t = np.linspace(0, timespan, timespan * sample_frequency)

sin_0 = sine_signal_generator(sample_frequency)(t)
sin_1 = sine_signal_generator(sample_frequency / 2)(t)
sin_2 = sine_signal_generator(sample_frequency / 4)(t)
sin_3 = sine_signal_generator(0)(t)

fig, axs = plt.subplots(4)
fig.tight_layout(pad=1.5)

axs[0].plot(t, sin_0)
axs[1].plot(t, sin_1)
axs[2].plot(t, sin_2)
axs[3].plot(t, sin_3)

fig.savefig(f'{OUT}/ex_6.pdf', format='pdf')
