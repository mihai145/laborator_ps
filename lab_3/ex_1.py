import numpy as np
import matplotlib.pyplot as plt
OUT = 'graphs'


# Verify that a N*N matrix F is orthogonal
def verify(F, N):
    R = 1/N * F * F.H - np.identity(N)

    for r in range(N):
        for c in range(N):
            if np.abs(R[r, c]) > 0.00000001:
                print(f'Wrong for {r, c}, got {R[r, c]}')

    print('OK, matrice ortogonala')


N = 8
F = np.matrix(np.zeros((N, N), np.complex256))
for r in range(N):
    for c in range(N):
        F[r, c] = np.exp(-2 * np.pi * 1j * c * r / N)

verify(F, N)

fig, axs = plt.subplots(N)
fig.tight_layout(pad=0)
fig.set_figheight(10)

for r in range(N):
    x = np.linspace(0, N - 1, N)
    y_real, y_imag = [np.real(F[r, c]) for c in range(N)], [np.imag(F[r, c]) for c in range(N)]
    axs[r].plot(x, y_real, 'r-', label='Re')
    axs[r].plot(x, y_imag, 'b--', label='Img')
    
    if r == N-1:
        handles, labels = axs[N-1].get_legend_handles_labels()
        fig.legend(handles, labels, loc='upper right')

fig.savefig(f'{OUT}/ex_1.png', format='png')
fig.savefig(f'{OUT}/ex_1.pdf', format='pdf')
