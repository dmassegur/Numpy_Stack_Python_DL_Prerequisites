import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filename = 'data_1d.csv'
A = pd.read_csv(filename, header = None).values  # converted straightaway to a matrix

x = A[:,0]
y = A[:,1]


# plt.scatter(x, y)

# plt.show()


## linear regression
x_line = np.linspace(0, 100, 100)
y_line = 2 * x_line + 1

plt.scatter(x, y, label='data set')
plt.plot(x_line, y_line, label='regression')
plt.legend(loc='right')
plt.grid(True)

plt.show()


## Histogram of x data: how many data points within bands.
plt.hist(x)  # default is 10 bands

plt.show()


## Random function
R = np.random.rand(10000)

plt.hist(R, 20)  # histogram in 20 bands; 
plt.show()
# idem:
plt.hist(R, bins=20)  # histogram in 20 bands; 
plt.show()


## Checking the linear regression is linearly distributed:
y_actual = 2*x + 1
residuals = y - y_actual

plt.hist(residuals, histtype='step')
plt.show()

# cumulative distribituion:
plt.hist(residuals, histtype='step', cumulative=1)
plt.show()
