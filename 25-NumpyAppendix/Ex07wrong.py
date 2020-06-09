import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import *
from builtins import zip


## Ex7: Generate Donuts


def Circlefunc(x, r):
    
    y_circ = np.sqrt( r**2 - x**2 )
    return y_circ


t0 = datetime.now()

# number of donuts:
n = 2

# random generation of the donut radius:
r = np.array([10, 20])  # np.random.rand(2)*20
     
i = 0
m = 1000
D = np.array([[]])
Dhalf = np.array([[]])
# generating the donuts in two halves:
for j in range(-1,2,2) : 
    # Random generation of the x value dataset , centred in x=0
    x = np.random.rand(m,1) * 2*r[i] - r[i]
    # x = (x - np.mean(x)) / (max(x)-min(x))  # x = x * 2*r[i] - r[i]
    # x = x * 2*r[i]
#     print(x.shape)
#     print(x[0:10,:])
#     print(max(x))
    
    
    # Generating the y value of the circle
    # y = np.array((x.shape[0],1))
    # k = 0
    # for j in x[:,0] :
    #     y[j] = Circlefunc(j, r[i])
    #     j += 1
    r_rand = r[i] + 0*np.random.rand(x.shape[0])*r[i]/10   # some randomness added to the radius
    y = j * Circlefunc(x[:,0], r_rand)     
    
    # appending y and radius values to the x array
#     print(x.shape)
#     print(np.array([y]).T.shape)
#     print(np.array([np.ones(x.shape[0])*r[i]]).T.shape)
    Dhalf = np.append( x, np.array([y]).T, axis=1 )
    Dhalf = np.append( Dhalf, np.array([np.ones(Dhalf.shape[0])*r[i]]).T, axis=1 )
    
    if j==-1 :
        D = Dhalf
    else :
        D = np.append(D, Dhalf, axis=0)
    
#     print(D.shape)
#     print(D[0:10,:])
    print(j)

print(D.shape)

# Plotting the result:
plt.scatter(D[:,0], D[:,1], c=D[:,2], s=20.0, alpha=0.3, label='XOR dataset')
plt.xlabel('feature x1')
plt.ylabel('feature x1')
plt.title('Donut dataset')
plt.axis('equal') 
plt.grid(True) 
# plt.legend()
plt.show()

dt = datetime.now() - t0



print('')
print( 'Donut dataset generation and plot, elapsed time: %0.4f seconds.' %(dt.total_seconds()) )
