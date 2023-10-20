import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'


def generate_sin(amplitude, frequency, phase):
    def sin(t):
        return amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return sin


def generate_cos(amplitude, frequency, phase):
    def cos(t):
        return amplitude * np.cos(2 * np.pi * frequency * t + phase)
    return cos


sin = generate_sin(amplitude=1, frequency=5, phase=np.pi/2)
cos = generate_cos(amplitude=1, frequency=5, phase=0)

t = np.linspace(0, 2, 500)
sin_t = sin(t)
cos_t = cos(t)

fig, axs = plt.subplots(2)
fig.tight_layout(pad=1.5)

axs[0].plot(t, sin_t)
axs[0].set_title('sin(10pi+pi/2)')

axs[1].plot(t, cos_t)
axs[1].set_title('cos(10pi)')

fig.savefig(f'{OUT}/ex_1.pdf', format='pdf')
