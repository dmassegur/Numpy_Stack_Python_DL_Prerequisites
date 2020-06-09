import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import norm


## Sampling from a normal random distribution

r = np.random.randn(10000)
print(norm.pdf(r))

plt.hist(r, bins=100, histtype='step')
plt.show()


## Sampling but with a non zero mean and different std:
# we jsut have to scale and move the data!
avg = 5  # desired mean
std = 10 # desired std
r = std*np.random.randn(10000) - 5

plt.hist(r, bins=100)
plt.show()


