import numpy as np
import matplotlib.pyplot as plt
OUT='graphs'

fig, axs = plt.subplots(2, 2)

x = np.random.rand(100)
for i in range(4):
    axs[i//2, i%2].plot(x)
    x = np.convolve(x, x)

fig.savefig(f'{OUT}/ex_1.pdf', format='pdf')
