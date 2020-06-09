import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


## Reading Kaggle data:

# Getting current directory:
currDir = os.getcwd()
print(currDir)

# print('C:\\U')
filename = 'train.csv'
filedir = 'C:\\Users\\FamilyMK\\Documents\\DAVID\\Kaggle'
filepath = filedir+'\\'+filename
print(filepath)
 
# Reading kaggle data set:
A = pd.read_csv(filepath).values  # by default, the first row of the file will be treated as header and thus, it will not be included as a data row.
 
print(A[0:4])
print(A.shape)


# Grab the first image of the dataset:
im = A[0, 1:]  # we exclude the first column as this is the label (y).  1: =  1:end

# we reshape the 1x784 vector to a matrix of 28x28
im = im.reshape(28, 28)
print(im.shape)


## Plotting the image:
plt.imshow(im)
plt.show()

print('')
print(A[0,0])  # y label of the first image


## Plotting in b&w:
plt.imshow(255-im, cmap='gray')  # I plot it inverted
plt.show()


# Grab a random image of the dataset:
rows = range(0,A.shape[0],1)
rows_rand = np.random.permutation(rows)
print('')
print(rows_rand[0:4])
i = rows_rand[0]
print(i)
im = A[i, 1:]  # we exclude the first column as this is the label (y).  1: =  1:end

# we reshape the 1x784 vector to a matrix of 28x28
im = im.reshape(28, 28)
print(im.shape)


## Plotting the image:
plt.imshow(im)
plt.show()

print(A[i,0])  # y label of the first image


## Plotting in b&w:
plt.imshow(255-im, cmap='gray')  # I plot it inverted
plt.show()



