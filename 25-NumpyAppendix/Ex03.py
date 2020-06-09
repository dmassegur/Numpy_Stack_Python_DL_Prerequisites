import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


## Ex3: plot the mean image for each of the digit classes of the mnist dataset


# Getting current directory:
currDir = os.getcwd()
print(currDir)

# print('C:\\U')
filename = 'train.csv'
filedir = 'C:\\Users\\FamilyMK\\Documents\\DAVID\\Kaggle'
filepath = filedir+'\\'+filename
print(filepath)
 
# Reading kaggle data set:
Mnist = pd.read_csv(filepath).values  # by default, the first row of the file will be treated as header and thus, it will not be included as a data row.

print(Mnist[0:4,0:10])



print('')
# looping for each class to sort out each image
num_class = 10
for i in range(0,num_class,1) :
    
    # getting the image index for digit i in the dataset (digit class value is stored in first column)
    idx = np.array(np.where(Mnist[:,0]==i))  # converted from tuple to 2d array
#     print(idx)
#     print(idx.shape)
       
    # summing the pixel value for only the indexed rows on each pixel position (column)
    mean_image = np.sum(Mnist[idx,:], axis=1) # row sum for each column
#     print(mean_image.shape)
#     print(mean_image)
    
    # average of all images:
    mean_image = mean_image / idx.shape[1]
    
    if i==0 :
      Mean_image = mean_image   # initializing Y with first row of x
    else :
      Mean_image = np.append(Mean_image, mean_image, axis=0)  # appending the following x rows
    
    
print(Mean_image[:,0:15])



# print('')
# # Reshaping the image from 1x784 vector to 28x28 matrix:
# mean_im = mean_image[0,1:].reshape( np.sqrt( mean_image.shape[1]-1 ).astype(int), np.sqrt( mean_image.shape[1]-1 ).astype(int) )
# print(mean_im.shape)
# 
# # plotting the mean image for the i class 
# plt.imshow(255-mean_im, cmap='gray')
# plt.show()

print('')
# Reshaping each image from 1x784 vector to 28x28 matrix:
for i in range(0,num_class,1) :
    mean_im = Mean_image[i,1:].reshape( np.sqrt( Mean_image.shape[1]-1 ).astype(int), np.sqrt( Mean_image.shape[1]-1 ).astype(int) )
#     print(mean_im.shape)

    # plotting the mean image for the i class 
    plt.imshow(255-mean_im, cmap='gray')
    plt.show()
