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

def CircleCylindricfunc(r, theta):
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    x = np.append(x, y, axis = 1)
    return x


t0 = datetime.now()

# # number of donuts:
# n = 2

# generation of the donut radius:
r = np.array([10, 20])  # np.random.rand(2)*20
     
i = 0
m = 500
D = np.array([[]])
# loop through all the donuts:

for i in range(0,r.shape[0],1) :
    
    # Random generation of the angles feature , centred in x=0
    theta = np.random.rand(m,1) * 2 * np.pi 
    #     print(theta.shape)
    #     print(theta[0:10,:])
    #     print(max(theta))
    
    
    # Generating the x and y values of the circle, given theta and radius
    r_rand = r[i]  +  (np.random.randn(theta.shape[0])-0.5) * r[i] / 16   # some randomness added to the radius
    r_rand = np.array([r_rand]).T
    xy = CircleCylindricfunc(r_rand, theta)     
    # print(xy.shape)
    
    
    # appending radius values to the x,y array
    xy = np.append( xy, np.array([np.ones(xy.shape[0])*r[i]]).T, axis=1 )
    
    # appending subsequent donuts
    if i == 0 :
        D = xy
    else :
        D = np.append(D, xy, axis = 0)


# print(D.shape)
# print(D[0:10,:])


# Plotting the result:
plt.scatter(D[:,0], D[:,1], c=D[:,2], s=40.0, alpha=0.3, label='Donut dataset')
plt.xlabel('feature x1')
plt.ylabel('feature x2')
plt.title('Donut dataset')
plt.axis('equal') 
plt.grid(True) 
# plt.legend()
plt.show()




## Writing it in Pandas

# First we creat the dataframe:
df = pd.DataFrame(D, columns=['x1','x2','y'])
print(df.head())

# Getting current directory:
currDir = os.getcwd()
# print(currDir)

# Assigning file path
filename = 'Donuts.csv'
filedir = currDir  # 'C:\\Users\\FamilyMK\\Documents\\DAVID\\Kaggle'
filepath = filedir+'\\'+filename
print(filepath)

# exporting to csv from pandas:
export_csv = df.to_csv(filepath, index=None, header=True)  # we don't write the row indices (there are none), we write the column headers



dt = datetime.now() - t0


print('')
print( 'Donut dataset generation and plot, elapsed time: %0.4f seconds.' %(dt.total_seconds()) )
