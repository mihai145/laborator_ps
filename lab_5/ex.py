import numpy as np
import matplotlib.pyplot as plt
import datetime

# a)
print(f'Frecventa de esantionare este {1/3600}Hz')

# b)
x = np.genfromtxt('Train.csv', delimiter=',')[1:]
N = len(x)
print(f'Intervalul de timp acoperit este {N} ore ({N//24} zile)')

# c)
print(f'In conditiile enuntate frecventa maxima este {1/7200}Hz')

# d)
X_sv = x[:,2].copy() # saved copy for i)

X = np.fft.fft(x[:,2])
X = abs(X/N)
X = X[:N//2]

f = (1/3600) * np.linspace(0, N/2, N//2) / N

plt.figure()
plt.stem(X)
plt.xticks(range(len(f))[::2000], [str(round(x, 5)) + 'Hz' for x in f[::2000]])
plt.savefig('fft.pdf', format='pdf')

# e)
print(f'Semnalul are o componenta continua, deoarece are media mai mare decat 0: {X[0]}')

x_elim = x[:,2] - np.mean(x[:,2])
X_elim = np.fft.fft(x_elim)
X_elim = abs(X_elim/N)
X_elim = X_elim[:N//2]

plt.figure()
plt.stem(X_elim)
plt.xticks(range(len(f))[::2000], [str(round(x, 5)) + 'Hz' for x in f[::2000]])
plt.savefig('fft_elim.pdf', format='pdf')

# f)
args = np.argsort(X_elim)[-5:]
for (idx, arg) in enumerate(args[::-1]):
    cnt_zile = (1/f[arg])/(24 * 3600)
    print(f'A {idx+1}-a cea mai insemnata frecventa corespunde unei perioade de {cnt_zile} zile')

# A 1-a cea mai insemnata frecventa corespunde unei perioade de 761.9166666666666 zile
# A 2-a cea mai insemnata frecventa corespunde unei perioade de 380.9583333333333 zile
# A 3-a cea mai insemnata frecventa corespunde unei perioade de 0.999890638670166 zile
# A 4-a cea mai insemnata frecventa corespunde unei perioade de 253.97222222222217 zile
# A 5-a cea mai insemnata frecventa corespunde unei perioade de 6.99006116207951 zile

# g)
with open('Train.csv') as file:
    dates = []
    for line in file.readlines():
        dates += [line.split(',')[1]]

def is_monday(date):
    d = datetime.datetime(int(date[6:10]), int(date[0:2]), int(date[3:5]))
    if d.strftime('%A') == 'luni':
        return True

cnt_samples_1_month = 30 * 24
samples_1_month = []
for i in range(1000, len(x)):
    if is_monday(dates[i]):
        for j in range(cnt_samples_1_month):
            samples_1_month += [x[i+j,2]]
        break

plt.figure()
plt.plot(samples_1_month)
plt.savefig('1_month.pdf', format='pdf')

# h)
# Putem analiza trendul de crestere a traficului, dupa care vom realiza masuratori in prezent. Apoi, vom estima perioada de inceput a studiului.
# Totusi, aceasta solutie asuma un trend constant de crestere a traficului si acuratete a masuratorilor din prezent.

# i)
X_cleared = np.fft.fft(X_sv)
for i in range(1, len(X_cleared)//2):
    cnt_zile = (1/f[i])/(24 * 3600)
    if cnt_zile < 1/3: # frecvente inalte, cel putin de 3 ori pe zi
        X_cleared[i:len(X_cleared)-i] = 0+0j
        break

cleared_signal = np.fft.ifft(X_cleared)

plt.figure()
fig, axs = plt.subplots(2)
fig.suptitle("500 masuratori consecutive: initial vs frecvente inalte eliminate")
axs[0].plot(X_sv[1000:1500])
axs[1].plot(cleared_signal[1000:1500].real)
plt.savefig('cleared_signal.pdf', format='pdf')
