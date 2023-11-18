import numpy as np
import matplotlib.pyplot as plt
import scipy
OUT="graphs"


# Read data from CSV
data = np.genfromtxt('Train.csv', delimiter=',', skip_header=True)

# a)
samples = 24 * 3
x = data[:samples]

# b)
plt.figure()
fig, axs = plt.subplots(5, figsize=(6, 10))
fig.tight_layout(pad=1.5)

for (idx, w) in enumerate([1, 5, 9, 13, 17]):
    x_w = np.convolve(x[:,2], np.ones(w), 'valid') / w
    axs[idx].plot(np.linspace(0, len(x_w) - 1, len(x_w)), x_w)
    axs[idx].set_title(f'w={w}')

fig.savefig(f'{OUT}/ex_4b.pdf', format='pdf')

# c)
# Supposing the sampling is efficient, than the sampling frequency is the Nyquist frequency => the Nyquist frequency is 1/3600 Hz
# Let's consider high frequency anything that happens at least once every three hours, i.e 1/3*3600 < fr < 1/3600
# Normalized frequency is 1/3

# d)
butter_a, butter_b = scipy.signal.butter(5, 1/3, 'low')
cheby_a, cheby_b = scipy.signal.cheby1(5, 5, 1/3, 'low')

# e)
plt.figure()
fig, axs = plt.subplots(3)
fig.tight_layout(pad=1.5)

# I would choose the Butterworth filter - it better preserves the trends in the raw data
butter_x = scipy.signal.filtfilt(butter_a, butter_b, x[:,2])
cheby_x = scipy.signal.filtfilt(cheby_a, cheby_b, x[:,2])

axs[0].plot(x[:,2])
axs[1].plot(butter_x)
axs[2].plot(cheby_x)

fig.savefig(f'{OUT}/ex_4e.pdf', format='pdf')

# f)
plt.figure()
fig, axs = plt.subplots(4, 2, figsize=(8, 8))
fig.tight_layout(pad=1.5)

butter_filters = [scipy.signal.butter(2, 1/3, 'low'), 
                  scipy.signal.butter(4, 1/3, 'low'), 
                  scipy.signal.butter(6, 1/3, 'low'), 
                  scipy.signal.butter(8, 1/3, 'low')]
butter_metadata = [2, 4, 6, 8]

cheby_filters = [scipy.signal.cheby1(3, 3, 1/3, 'low'), 
                scipy.signal.cheby1(3, 7, 1/3, 'low'),
                scipy.signal.cheby1(7, 3, 1/3, 'low'), 
                scipy.signal.cheby1(7, 7, 1/3, 'low')]
cheby_metadata = [(3, 3), (3, 7), (7, 3), (7, 7)]

for (idx, filter) in enumerate(butter_filters):
    y = scipy.signal.filtfilt(filter[0], filter[1], x[:,2])
    axs[idx, 0].plot(y)
    axs[idx, 0].set_title(f'Butter wn={butter_metadata[idx]}')

for (idx, filter) in enumerate(cheby_filters):
    y = scipy.signal.filtfilt(filter[0], filter[1], x[:,2])
    axs[idx, 1].plot(y)
    axs[idx, 1].set_title(f'Cheby wn={cheby_metadata[idx][0]}, rp={cheby_metadata[idx][1]}')

fig.savefig(f'{OUT}/ex_4f.pdf', format='pdf')
