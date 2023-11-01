import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'


# Signal function, has frequences of 3Hz, 5Hz and 8Hz
signal = lambda x: 1/2 * np.cos(2 * np.pi * 3 * x + np.pi / 2) \
                    + np.cos(2 * np.pi * 5 * x) \
                    + 3 * np.cos(2 * np.pi * 8 * x)

# Used for plotting the signal
t_desen = np.linspace(0, 1, 1024)
f_desen = signal(t_desen)

# For 10 samples, we should see leakage
# For 20 samples, the abs() of output values should clearly show base frequencies
for CNT_SAMPLES in [10, 20]:
    # Observed samples
    t = np.linspace(0, 1, CNT_SAMPLES + 1)
    f = signal(t)

    # Fourier matrix
    F = np.matrix(np.zeros((CNT_SAMPLES, CNT_SAMPLES), np.complex256))
    for r in range(CNT_SAMPLES):
        for c in range(CNT_SAMPLES):
            F[r, c] = np.exp(-2 * np.pi * 1j * c * r / CNT_SAMPLES)

    fig, axs = plt.subplots(1, 2)
    fig.tight_layout(pad=1.5)

    axs[0].set_title('Signal')
    axs[0].plot(t_desen, f_desen)

    X = np.matmul(F, f[:-1])
    axs[1].set_title('Frecventa')
    # Show only half of the frequencies in the transform - it is symmetrical
    axs[1].stem([i for i in range(X.shape[1] // 2)], [np.abs(X[0,i]) for i in range(X.shape[1] // 2)])

    name = "ex_3"
    if CNT_SAMPLES == 10:
        name += "_leakage"
    
    fig.savefig(f'{OUT}/{name}.pdf', format='pdf')
    fig.savefig(f'{OUT}/{name}.png', format='png')
    plt.close()
