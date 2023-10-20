import numpy as np
import matplotlib.pyplot as plt

OUT = 'graphs'

# Lab 1 2a)
def sine_signal_generator(freq):
    def generate_f(t):
        return np.sin(freq * 2 * np.pi * t)
    return generate_f
sine_5hz = sine_signal_generator(5)

# Lab 1 2c)
def sawtooth_signal_generator(freq):
    def generate_f(t):
        spread_out = t * 2 * freq
        regions = np.mod(np.floor(spread_out), 2)
        return -regions + spread_out - np.floor(spread_out)
    return generate_f
sawtooth_5hz = sawtooth_signal_generator(5)

t = np.linspace(0, 1, 500)

fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)

axs[0].set_title('sine_5hz + sawtooth_5hz')
axs[0].plot(t, sine_5hz(t) + sawtooth_5hz(t))

axs[1].set_title('sine_5hz')
axs[1].plot(t, sine_5hz(t))

axs[2].set_title('sawtooth_5hz')
axs[2].plot(t, sawtooth_5hz(t))

fig.savefig(f'{OUT}/ex_4.pdf', format='pdf')
