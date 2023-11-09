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
X = np.fft.fft(x[:,2])
X_sv = X.copy() # for i)
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

# i)
