import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
OUT="graphs"

_, x = scipy.io.wavfile.read("AEIOU.wav")
arr = x[:,0]

groups = []
for i in range(0, len(arr), (len(arr) // 100) // 2):
    if i + len(arr)//100 >= len(arr):
        continue
    groups += [arr[i : i + len(arr)//100 + 1]]

fft_outputs = []
for group in groups:
    fft_outputs += [np.fft.fft(group)]

spectogram = np.zeros((len(fft_outputs), len(fft_outputs[0]) // 2))
for l, fft_output in enumerate(fft_outputs):
    for c, x in enumerate(fft_output[:len(fft_output)//2]):
        spectogram[l][c] = np.abs(x)

plt.imshow(spectogram.T, norm="log", aspect=0.2)
plt.savefig(f'{OUT}/ex_6.pdf', format='pdf')
plt.savefig(f'{OUT}/ex_6.png', format='png')
