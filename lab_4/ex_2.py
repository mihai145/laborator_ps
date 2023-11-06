import numpy as np
import matplotlib.pyplot as plt
OUT = "graphs"

# Frecventa originala 4Hz
signal_4hz = lambda x: np.sin(2 * np.pi * 4 * x)
signal_10hz = lambda x: np.sin(2 * np.pi * 10 * x)
signal_16hz = lambda x: np.sin(2 * np.pi * 16 * x)

# Desen
t_desen = np.linspace(0, 1, 1000 + 1)
f_desen = signal_4hz(t_desen)

cnt_samples = 6 # sub-Nyquist
t = np.linspace(0, 1, cnt_samples + 1)
f = signal_4hz(t)

fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)

axs[0].plot(t_desen, f_desen)
axs[0].stem(t, f)

t_desen_10hz = np.linspace(0, 1, 1000 + 1)
f_desen_10hz = signal_10hz(t_desen_10hz)
axs[1].plot(t_desen_10hz, f_desen_10hz)
axs[1].stem(t, f)

t_desen_16hz = np.linspace(0, 1, 1000 + 1)
f_desen_16hz = signal_16hz(t_desen_16hz)
axs[2].plot(t_desen_16hz, f_desen_16hz)
axs[2].stem(t, f)

fig.suptitle('Sub-Nyquist -> exista confuzie')
fig.savefig(f'{OUT}/ex_2.pdf', format='pdf')
fig.savefig(f'{OUT}/ex_2.png', format='png')
