import numpy as np
import scipy
OUT = 'sounds'


# Lab 1 2c)
def sawtooth_signal_generator(freq):
    def generate_f(t):
        spread_out = t * 2 * freq
        regions = np.mod(np.floor(spread_out), 2)
        return -regions + spread_out - np.floor(spread_out)
    return generate_f

sawtooth_10hz = sawtooth_signal_generator(10)
sawtooth_5hz = sawtooth_signal_generator(5)

t = np.linspace(0, 1, 500000)
mixed = np.append(sawtooth_10hz(t), sawtooth_5hz(t))

rate = int(1e5)
scipy.io.wavfile.write(f'{OUT}/ex_5.wav', rate, mixed)

# A doua portiune de sunet este mai lenta decat prima (dilatata)
