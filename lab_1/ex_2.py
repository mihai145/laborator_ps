import numpy as np
import matplotlib.pyplot as plt
out = "graphs"
fig_cnt = 0

# a)
def sine_signal_generator(freq):
    def generate_f(t):
        return np.sin(freq * 2 * np.pi * t)
    return generate_f

sine_400hz = sine_signal_generator(400)
# alegem un interval foarte mic pentru a putea distinge oscilatiile
# avem foarte multe esantioane, nu le vom putea distinge intre ele
# alegerea unui numar mai mic de esantioane (<= 100) ajuta la distingerea lor
for cnt_samples in [1600, 100]:
    t, sampled_t = np.linspace(0, 0.01, 10000), np.linspace(0, 0.01, cnt_samples)
    signal, sampled_signal = sine_400hz(t), sine_400hz(sampled_t)

    fig_cnt += 1
    plt.figure(fig_cnt)
    plt.plot(t, signal)
    plt.stem(sampled_t, sampled_signal)

    plt.title(f'Sine 400hz cu {cnt_samples} esantioane')
    plt.savefig(f'{out}/ex_2_a_{cnt_samples}_esantioane.pdf')
    plt.close(fig_cnt)

# b)
# ar trebui sa vedem 3*800=2400 de oscilatii in 3 secunde
# pentru lizibilitate, generam doar 200 de puncte, deci vom "rata" oscilatii
sine_800hz = sine_signal_generator(800)
t = np.linspace(0, 3, 200)
signal = sine_800hz(t)

fig_cnt += 1
plt.figure(fig_cnt)
plt.plot(t, signal)
plt.title('Sine 800hz pe interval de 3s')
plt.savefig(f'{out}/ex_2_b.pdf')
plt.close(fig_cnt)

# c)
def sawtooth_signal_generator(freq):
    def generate_f(t):
        spread_out = t * 2 * freq
        regions = np.mod(np.floor(spread_out), 2)
        return -regions + spread_out - np.floor(spread_out)
    return generate_f

sawtooth_240hz = sawtooth_signal_generator(240)
t = np.linspace(0, 0.05, 1000)
signal = sawtooth_240hz(t)

fig_cnt += 1
plt.figure(fig_cnt)
plt.plot(t, signal)
plt.title('Sawtooth 240hz')
plt.savefig(f'{out}/ex_2_c.pdf')
plt.close(fig_cnt)

# d)
def square_signal_generator(freq):
    def generate_f(t):
        spread_out = t * 2 * freq
        regions = np.mod(np.floor(spread_out), 2)
        regions[regions==1]=-1
        regions[regions==0]=1
        return regions
    return generate_f

square_300hz = square_signal_generator(300)
t = np.linspace(0, 0.05, 1000)
signal = square_300hz(t)

fig_cnt += 1
plt.figure(fig_cnt)
plt.plot(t, signal)
plt.title('Square 300hz')
plt.savefig(f'{out}/ex_2_d.pdf')
plt.close(fig_cnt)

# e)
rand_2d = np.random.rand(128, 128)
plt.title('Semnal 2d aleator')
plt.imshow(rand_2d)
plt.savefig(f'{out}/ex_2_e.pdf')

# f)
signal_2d = np.empty((128, 128))
for i in range(128):
    signal_2d[i,:] = np.sin(i) * np.cos(np.arange(0, 128, 1))
plt.title('Semnal 2d sin(x)*cos(y)')
plt.imshow(signal_2d)
plt.savefig(f'{out}/ex_2_f.pdf')
