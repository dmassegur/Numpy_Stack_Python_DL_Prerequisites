import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filename = 'data_1d.csv'
A = pd.read_csv(filename, header = None).values  # converted straightaway to a matrix

x = A[:,0]
y = A[:,1]

plt.scatter(x, y)

plt.show()


## linear regression
x_line = np.linspace(0, 100, 100)
y_line = 2 * x_line + 1

plt.scatter(x, y, label='data set')
plt.plot(x_line, y_line, label='regression')
plt.legend(loc='right')
plt.grid(True)

plt.show()