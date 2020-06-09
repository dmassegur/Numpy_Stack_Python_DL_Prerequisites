import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # linear spacing from 0 to 10 in 100 points.

y = np.sin(x)

plt.plot(x, y)

plt.show()  # now it shows the plot


plt.plot(x, y, label='sine')
plt.xlabel('Time [s]')
plt.ylabel('Sinus of time')
plt.title('Sinus chart')
plt.legend()

plt.show()  # now it shows the plot



