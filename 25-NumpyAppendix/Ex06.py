import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import *
from builtins import zip


## Ex7: Generate Donuts


def XORfunc(x1, x2):
    
    result = 1
    if ( (x1>0.5 and x2>0.5) or (x1<0.5 and x2<0.5) ) :
        result = 0

    return result


t0 = datetime.now()

# Random genration of the dataset
A = np.random.rand(10000,2)
print(A.shape)
print(A[0:10,:])

avg_1 = np.mean(A[:,0])
avg_2 = np.mean(A[:,1])
std_1 = np.std(A[:,0])
std_2 = np.std(A[:,1])


# Generating the XOR labels
k = 0
xor_result = np.zeros((A.shape[0],1))
for i,j in zip(A[:,0], A[:,1]) :
    xor_result[k] = XORfunc(i, j)
    k += 1

# Scaling and moving the dataset
A = A - A.mean()  # A = A * 2 - 1
A *= 2
print('Dataset feature 1: mean = %0.2f, std = %0.2f' %(avg_1, std_1))
print('Dataset feature 2: mean = %0.2f, std = %0.2f' %(avg_2, std_2))


# Appending the XOR labels
A = np.append(A, xor_result, axis=1)
print(A.shape)
print(A[0:10,:])

# Plotting the result:
plt.scatter(A[:,0], A[:,1], c=A[:,2], s=20.0, alpha=0.3, label='XOR dataset')
plt.xlabel('feature x1')
plt.ylabel('feature x1')
plt.title('XOR dataset')
# plt.legend()
plt.show()




## Writing it in Pandas

# First we creat the dataframe:
df = pd.DataFrame(A, columns=['x1','x2','y'])
print(df.head())

# Getting current directory:
currDir = os.getcwd()
# print(currDir)

# Assigning file path
filename = 'XOR.csv'
filedir = currDir  # 'C:\\Users\\FamilyMK\\Documents\\DAVID\\Kaggle'
filepath = filedir+'\\'+filename
print(filepath)

# exporting to csv from pandas:
export_csv = df.to_csv(filepath, index=None, header=True)  # we don't write the row indices (there are none), we write the column headers



dt = datetime.now() - t0


print('')
print( 'XOR dataset generation, elapsed time: %0.4f seconds.' %(dt.total_seconds()) )
