import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
import time
OUT = "graphs"

# Signal function
signal = lambda x: 1/2 * np.cos(2 * np.pi * 3 * x + np.pi / 2) \
                    + np.cos(2 * np.pi * 5 * x) \
                    + 3 * np.cos(2 * np.pi * 8 * x)

input_dimensions = [128, 256, 512, 1024, 2048, 4096, 8192]
naive_time, fft_time = [], []
for N in input_dimensions:
    t = np.linspace(0, 1, N + 1)[:-1]
    f = signal(t)

    t0 = time.time()

    # Naive implementation
    F = np.matrix(np.zeros((N, N), np.complex256))
    for r in range(N):
        for c in range(N):
            F[r, c] = np.exp(-2 * np.pi * 1j * c * r / N)
    X = np.matmul(F, f)

    t1 = time.time()

    # FFT
    X = fft.fft(f)
    t2 = time.time()

    naive_time += [t1 - t0]
    fft_time += [t2 - t1]

plt.title("Naive DFT vs FFT")
plt.plot(input_dimensions, np.log(naive_time))
plt.plot(input_dimensions, np.log(fft_time))
plt.savefig(f'{OUT}/ex_1.pdf', format='pdf')
plt.savefig(f'{OUT}/ex_1.png', format='png')
