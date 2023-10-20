import numpy as np
import scipy
import sounddevice
OUT = 'sounds'


# Lab 1 2a)
def sine_signal_generator(freq):
    def generate_f(t):
        return np.sin(freq * 2 * np.pi * t)
    return generate_f
sine_400hz = sine_signal_generator(400)

# Lab 1 2b)
sine_800hz = sine_signal_generator(800)

# Lab 1 2c)
def sawtooth_signal_generator(freq):
    def generate_f(t):
        spread_out = t * 2 * freq
        regions = np.mod(np.floor(spread_out), 2)
        return -regions + spread_out - np.floor(spread_out)
    return generate_f
sawtooth_240hz = sawtooth_signal_generator(240)

# Lab 1 2d)
def square_signal_generator(freq):
    def generate_f(t):
        spread_out = t * 2 * freq
        regions = np.mod(np.floor(spread_out), 2)
        regions[regions==1]=-1
        regions[regions==0]=1
        return regions
    return generate_f
square_300hz = square_signal_generator(300)

t = np.linspace(0, 1, 500000)

rate = int(1e5)
scipy.io.wavfile.write(f'{OUT}/sine_400.wav', rate, sine_400hz(t))
scipy.io.wavfile.write(f'{OUT}/sine_800.wav', rate, sine_800hz(t))
scipy.io.wavfile.write(f'{OUT}/sawtooth_240.wav', rate, sawtooth_240hz(t))
scipy.io.wavfile.write(f'{OUT}/square_300.wav', rate, square_300hz(t))

rate, x = scipy.io.wavfile.read(f'{OUT}/sawtooth_240.wav')
sounddevice.play(x, 44100)
