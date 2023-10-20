import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'


def generate_sin(amplitude, frequency, phase):
    def sin(t):
        return amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return sin


sin_1 = generate_sin(1, 2, 0)
sin_2 = generate_sin(1, 2, np.pi/2)
sin_3 = generate_sin(1, 2, np.pi)
sin_4 = generate_sin(1, 2, 3*np.pi/2)

t = np.linspace(0, 1, 500)

plt.figure(1)
plt.plot(t, sin_1(t))
plt.plot(t, sin_2(t))
plt.plot(t, sin_3(t))
plt.plot(t, sin_4(t))

plt.savefig(f'{OUT}/ex_2.pdf', format='pdf')
plt.close(1)

z = np.random.normal(0, 1, size=(len(t)))

plt.figure(2)
fig, axs = plt.subplots(4)
fig.tight_layout(pad=2)

for idx, snr in enumerate([0.1, 1, 10, 100]):
    phi = np.sqrt(1/snr * (np.linalg.norm(sin_1(t))**2)/(np.linalg.norm(z)**2))
    axs[idx].plot(t, sin_1(t) + phi * z)
    axs[idx].set_title(f'SNR = {snr}')

fig.savefig(f'{OUT}/ex_2_noise.pdf', format='pdf')
