import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import norm
from scipy.stats import multivariate_normal as mvn


## Load mat
## scipy.io.loadmat


## Audio  (WAV files)
## read: scipy.io.wavfile.read
## write: scipy.io.wavfile.write
## WAV files contain an amplitude at each time step. 44.1kHz = 44100 amplitude values per second  


## Signal processing
## scipy.signal
## Convolution
## convolve2d()


## FFT is in numpy!
x = np.linspace(0, 100, 10000)
# generating a signal of multiple frequencies:
y = np.sin(x) + np.sin(3*x) + np.sin(5*x)

plt.plot(x,y)
plt.show()

# FFT:
Y = np.fft.fft(y)
print(Y.shape)
print(Y)

plt.plot(abs(Y)) # we need to find the magnitude of the fft. because fft contains imaginary numbers
plt.show()

# calculate the frequencies (from the plot):
# reminder: sin(x) frequency = 1/2pi
print( '1st frequency: %0.1f -> first mode: %0.2f' %(16, 16 * 2*np.pi/100) )
print( '2nd frequency: %0.1f -> first mode: %0.2f' %(48.0, 48 * 2*np.pi/100) )
print( '3rd frequency: %0.1f -> first mode: %0.2f' %(80.0, 80 * 2*np.pi/100) )