import numpy as np


# generate random polynomials
p = np.random.randint(0, 10 + 1, 100)
q = np.random.randint(0, 10 + 1, 100)

# naive implementation
res_quadratic = np.zeros(len(p) + len(q) - 1, dtype=int)
for i in range(len(p)):
    for j in range(len(q)):
        res_quadratic[i + j] += p[i] * q[j]

# FFT
ext_p = np.zeros(len(p) + len(q) - 1)
ext_p[:len(p)] = p

ext_q = np.zeros(len(p) + len(q) - 1)
ext_q[:len(q)] = q

fft_p = np.fft.fft(ext_p)
fft_q = np.fft.fft(ext_q)
freq_prod = fft_p * fft_q
res_fft = np.real(np.fft.ifft(freq_prod))

# Differences
diff = res_quadratic - res_fft
print(f'Norma vectorului diferenta: {np.linalg.norm(diff)}')
