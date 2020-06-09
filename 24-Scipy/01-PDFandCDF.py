import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import norm


## PDF = Probability Density Function:

# probability density of 0 from a normal distribution
print(norm.pdf(0))

# probability density of 0 from a normal distribution with avg=5 and std=10
print(norm.pdf(0, loc=5, scale=10)) # loc=mean,  scale=std


r = np.random.randn(10000)
print(norm.pdf(r))

plt.hist(r, bins=100, histtype='step')  # not filled
plt.show()


## Log PDF:  the logarithmic of the probability
print(norm.logpdf(r))



## CFD = Cumulative Distribution Function:
print(norm.cdf(r))
print(norm.logcdf(r))

# plotting the cumulative distribution
plt.hist(r, bins=100, cumulative=1)
plt.show()