import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import norm


## Sampling from a normal random distribution in MULTIPLE DIMENSIONS

r = np.random.randn(10000, 2)  # creates two columns of 10000 random number rows
print(norm.pdf(r))

# We can't use hist anymore but scatter
plt.scatter(r[:,0], r[:,1])  
plt.axis('equal')  # this makes the same scale in x and y
plt.title('points should show a circle shape')
plt.show()  # this should be a circle


# if we tweak the std in each axis, it will have an ellyptical shape:
r[:,1] = 2.5*r[:,1] - 2  # we tweak mean std on one of the dimensions:

plt.scatter(r[:,0], r[:,1])  
plt.axis('equal')
plt.title('points should show an elliptical shape')
plt.show()  # this should be elliptical because we have 'squeezed' one axis

