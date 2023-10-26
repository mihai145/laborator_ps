import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'


# Lab 1a)
def cos_signal_generator(freq):
    def generate_f(t):
        return np.cos(freq * 2 * np.pi * t)
    return generate_f


freq, samples = 7, 10000
cos_7hz = cos_signal_generator(freq)

x = np.linspace(0, 1, samples)
y = cos_7hz(x)
ex = np.exp(-2 * np.pi * 1j * x)
y_ex = y * ex

# Figure 1
fig, axs = plt.subplots(1, 2)
fig.tight_layout(pad=3)
fig.suptitle('Cos 7Hz')

axs[0].plot(x, y)
axs[0].set_aspect('equal')
axs[0].set_ylabel('Amplitudine')
axs[0].set_xlabel('Timp')

axs[1].plot(np.real(y_ex), np.imag(y_ex))
axs[1].set_aspect('equal')
tolerance = 0.1
axs[1].set_xlim(-1 - tolerance, 1 + tolerance)
axs[1].set_ylim(-1 - tolerance, 1 + tolerance)
axs[1].axhline(y=0, color='black', linestyle='--')
axs[1].axvline(x=0, color='black', linestyle='--')
axs[1].set_ylabel('Imaginar')
axs[1].set_xlabel('Real')

fig.savefig(f'{OUT}/ex_2_fig_1.pdf', format='pdf')
fig.savefig(f'{OUT}/ex_2_fig_1.png', format='png')
plt.close()

# Figure 2
fig, axs = plt.subplots(2, 2)
fig.tight_layout(pad=1.75)

for (idx, freq) in enumerate([1, 2, 5, 7]):
    ex = np.exp(-2 * np.pi * 1j * freq * x)
    y_ex = y * ex
    axs[idx // 2][idx % 2].plot(np.real(y_ex), np.imag(y_ex))
    axs[idx // 2][idx % 2].set_aspect('equal')
    axs[idx // 2][idx % 2].set_xlim(-1 - tolerance, 1 + tolerance)
    axs[idx // 2][idx % 2].set_ylim(-1 - tolerance, 1 + tolerance)
    axs[idx // 2][idx % 2].axhline(y=0, color='black', linestyle='--')
    axs[idx // 2][idx % 2].axvline(x=0, color='black', linestyle='--')
    axs[idx // 2][idx % 2].set_ylabel('Imaginar')
    axs[idx // 2][idx % 2].set_xlabel('Real')

fig.savefig(f'{OUT}/ex_2_fig_2.pdf', format='pdf')
fig.savefig(f'{OUT}/ex_2_fig_2.png', format='png')
plt.close()
