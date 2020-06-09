import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import norm
from scipy.stats import multivariate_normal as mvn


## Sampling from a multivariate dimensions but correlated to each other (covariance)

# Covariance matrix example!
covar = np.array([[1, 0.8], [0.8, 3]])
# variance of 1 in the first dimension (var33=1)
# variance of 3 in the second dimension (var22=3)
# and a covariance of 0.8 between the two dimensions (var12=var21=0.8=covar)

# Mean example:
mu = np.array([0, 2])
# the mean on the 1st dimension is = 0
# the mean on the 2nd dimension is = 2


####!!! rvs function from mvn: draw random samples from a multivariate normal distribution!
r = mvn.rvs(mean=mu, cov= covar, size=1000)
# this generate a random dataset of the dimension in the vector mu, with mean from mu, covariance matrix from covar and will generate 1000 sample points.

plt.grid()
plt.scatter(r[:,0], r[:,1])
plt.title('multivariate randomly distributed points')
plt.axis('equal')
# we can see a bit of correlation between the two axis --> which is the 0.8 covariance!!
plt.show()


# There is a way to draw these samples in numpy, instead of scipy rvs
r = np.random.multivariate_normal(mean= mu, cov= covar, size=1000)

plt.scatter(r[:,0], r[:,1])
plt.title('multivariate randomly distributed points')
plt.axis('equal')
plt.grid()
# we can see a bit of correlation between the two axis --> which is the 0.8 covariance!!
plt.show()
