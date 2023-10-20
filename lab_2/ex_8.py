import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'

t = np.linspace(-np.pi / 2, np.pi / 2, 1000)

plt.figure(1)
fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)

axs[0].plot(t, np.sin(t))
axs[0].set_title('sin(a)')
axs[1].plot(t, t)
axs[1].set_title('a')
axs[2].plot(t, (t - 7 / 60 * t**3) / (1 + t**2 / 20))
axs[2].set_title('Pade')

fig.savefig(f'{OUT}/ex_8.pdf', format='pdf')
plt.close(1)

plt.figure(2)
fig, axs = plt.subplots(2)
fig.tight_layout(pad=1.5)

axs[0].plot(t, np.abs(t - np.sin(t)))
axs[0].set_title('Eroare sin(a) = a')
axs[1].plot(t, np.abs((t - 7 / 60 * t**3) / (1 + t**2 / 20) - np.sin(t)))
axs[1].set_title('Eroare Pade sin(a)')

fig.savefig(f'{OUT}/ex_8_eroare.pdf', format='pdf')
plt.close(2)
