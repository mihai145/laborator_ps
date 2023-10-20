import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'

# Lab 1 2a)
def sine_signal_generator(freq):
    def generate_f(t):
        return np.sin(freq * 2 * np.pi * t)
    return generate_f

sine_50hz = sine_signal_generator(50)

cnt_samples = 1000
t = np.linspace(0, 1, cnt_samples)
t_4 = np.linspace(0, 1, cnt_samples // 4)
t_16 = np.linspace(0, 1, cnt_samples // 4 // 4)

fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)

axs[0].plot(t, sine_50hz(t))
axs[0].set_title('Semnal esantionat 1000 samples')
axs[1].plot(t_4, sine_50hz(t_4))
axs[1].set_title(f'Semnal esantionat {1000//4} samples')
axs[2].plot(t_16, sine_50hz(t_16))
axs[2].set_title(f'Semnal esantionat {1000//16} samples')

fig.savefig(f'{OUT}/ex_7.pdf', format='pdf')

# Observam ca pe masura ce decimam semnalul, acesta este din ce in ce mai putin asemanator cu semnalul real
# Mai mult, nu mai putem nici macar aproxima perioada semnalului real
