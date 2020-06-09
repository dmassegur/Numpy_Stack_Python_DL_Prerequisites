import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import *
from builtins import zip


## Ex8: Generate Spiral dataset


def Circlefunc(x, r):
    
    y_circ = np.sqrt( r**2 - x**2 )
    return y_circ

def CircleCylindricfunc(r, theta):
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    x = np.append(x, y, axis = 1)
    return x



t0 = datetime.now()


# number of points per spiral branch:
m = 175

# Generating a spiral branch:
t = np.array([np.linspace(0,1,m)]).T
# print(t.shape)

# offset angles for each branch of the first spiral:
theta_rot = np.array([[0, 360/3*1, 360/3*2 ]]) - 30
# the second spiral is offset to be in between:
theta_rot = np.append(theta_rot, theta_rot+(theta_rot[0,1]-theta_rot[0,0])/2 , axis=0)

# starting and end radius of each branch:
r_ends = np.array([1.5, 15]);


# creating the j branch of the i spiral via a loop:
D = np.array([[]])
for i in range(0,theta_rot.shape[0],1) :  # i= 0  # spiral row
    for j in range(0,theta_rot.shape[1],1) :  # j = 0  # branch col

        # spiral angle goes from 0 to 45 degrees.
        theta = t * np.pi / 3 + (theta_rot[i,j] / 180 * np.pi) 
        # theta += np.array([ ( np.random.randn(theta.shape[0]) - 0.5 ) * 2*np.pi/50 ]).T
#         print(theta.shape)
        
        # spiral radius
        r = t * (r_ends[1]-r_ends[0]) + r_ends[0]
        # r += np.array([ ( np.random.randn(r.shape[0]) - 0.5 ) * np.max(r_ends)/10 ]).T
#         print(r.shape)
        
        # coordinates of the spiral:
        xy = CircleCylindricfunc(r, theta) 
        xy += (np.random.randn(xy.shape[0],xy.shape[1]) - 0.5) / 1.5
        
        # appending radius values to the x,y array
        xy = np.append( xy, np.array([np.ones(xy.shape[0])*i]).T, axis=1 )
#         print(xy.shape)
        
        # storing everythin in a big dataset matrix of mx3
        if i==0 and j==0 :
            D = xy
        else :
            D = np.append(D, xy, axis=0)
  
  
    
# print(D.shape)
# Plotting the result:
plt.scatter(D[:,0], D[:,1], c=D[:,2], s=40.0, alpha=0.3, label='Spiral dataset')
plt.xlabel('feature x1')
plt.ylabel('feature x2')
plt.title('Spiral dataset')
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
filename = 'Spiral.csv'
filedir = currDir  # 'C:\\Users\\FamilyMK\\Documents\\DAVID\\Kaggle'
filepath = filedir+'\\'+filename
print(filepath)

# exporting to csv from pandas:
export_csv = df.to_csv(filepath, index=None, header=True)  # we don't write the row indices (there are none), we write the column headers



dt = datetime.now() - t0


print('')
print( 'Spiral dataset generation and plot, elapsed time: %0.4f seconds.' %(dt.total_seconds()) )
