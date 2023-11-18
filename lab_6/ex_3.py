import numpy as np
import matplotlib.pyplot as plt
OUT='graphs'


# Original signal
t = np.linspace(0, 0.1, 300)
f = np.sin(2 * np.pi * 100 * t)

# Rectangular window
w_rect = np.zeros(300)
w_rect[50:250] = 1
f_rect = f * w_rect

# Hanning window
w_hanning = np.zeros(300)
w_hanning[50:250] = 0.5 * (1 - np.cos(2 * np.pi * np.linspace(0, 199, 200) / 200))
f_hanning = f * w_hanning

fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)

axs[0].plot(t, f)
axs[0].set_title('Original signal')
axs[1].plot(t, f_rect)
axs[1].set_title('Rectangular window')
axs[2].plot(t, f_hanning)
axs[2].set_title('Hanning window')

fig.savefig(f'{OUT}/ex_3.pdf', format='pdf')
