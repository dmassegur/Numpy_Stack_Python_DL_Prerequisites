import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import *


## Ex4: plot the mean image ROTATED 90degrees for each of the digit classes of the mnist dataset


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
# Reshaping each mean image from 1x784 vector to 28x28 matrix:
class_id = 4
t0 = datetime.now()
# for i in range(0,num_class,1) :
for i in range(class_id,class_id+1,1) :
    
    mean_im = Mean_image[i,1:].reshape( np.sqrt( Mean_image.shape[1]-1 ).astype(int), np.sqrt( Mean_image.shape[1]-1 ).astype(int) )
#     print(mean_im.shape)
 
    # plotting the mean image for the i class 
    plt.imshow(255-mean_im, cmap='gray')
    plt.show()
     
    # image rotations
    mean_im_orig = mean_im 
     
    # 90deg rotation clockwise
    mean_im = mean_im_orig[range(mean_im_orig.shape[0]-1,-1,-1) , :]
    mean_im = mean_im.T  # with 
    plt.imshow(255-mean_im, cmap='gray')
    plt.show()
  
    # 180deg rotation
    mean_im = mean_im_orig[range(mean_im_orig.shape[0]-1,-1,-1) , :]
    mean_im = mean_im[: , range(mean_im.shape[1]-1,-1,-1)]
#     print(mean_im.shape)
    plt.imshow(255-mean_im, cmap='gray')
    plt.show()
     
    # 90deg rotation anticlockwise
    mean_im = mean_im_orig.T  
    mean_im = mean_im[range(mean_im.shape[0]-1,-1,-1) , :]
#     print(mean_im.shape)
    plt.imshow(255-mean_im, cmap='gray')
    plt.show()

dt = datetime.now() - t0

print( ' Image rotation -> elapsed execution time: %0.4f seconds.' %(dt.total_seconds()) )


# Image rotation but with for loops:
t0 = datetime.now()
# for i in range(0,num_class,1) :
for i in range(class_id,class_id+1,1) :
    
    mean_im = Mean_image[i,1:].reshape( np.sqrt( Mean_image.shape[1]-1 ).astype(int), np.sqrt( Mean_image.shape[1]-1 ).astype(int) )
#     print(mean_im.shape)

    # plotting the mean image for the i class 
    plt.imshow(255-mean_im, cmap='gray')
    plt.show()
    
    # image rotations
    mean_im_orig = mean_im 
#     plt.imshow(255-mean_im_orig, cmap='gray')
#     plt.show()
    mean_im2 = np.zeros((mean_im_orig.shape[0], mean_im_orig.shape[1]))
    mean_im3 = np.zeros((mean_im_orig.shape[0], mean_im_orig.shape[1]))
#     print(mean_im2.shape)
    
    # 90deg rotation clockwise
    for i in range(0,mean_im_orig.shape[0],1) :
        for j in range(0,mean_im_orig.shape[1],1) :
            mean_im2[mean_im_orig.shape[0]-1-i,j] = mean_im_orig[i,j]
    for i in range(0,mean_im_orig.shape[0],1) :
        for j in range(0,mean_im_orig.shape[1],1) :
            mean_im3[j,i] = mean_im2[i,j]
    plt.imshow(255-mean_im3, cmap='gray')
    plt.show()
 
    # 180deg rotation
    for i in range(0,mean_im_orig.shape[0],1) :
        for j in range(0,mean_im_orig.shape[1],1) :
            mean_im2[mean_im_orig.shape[0]-1-i,j] = mean_im_orig[i,j]
    for i in range(0,mean_im_orig.shape[0],1) :
        for j in range(0,mean_im_orig.shape[1],1) :
            mean_im3[i,mean_im_orig.shape[1]-1-j] = mean_im2[i,j]
#     print(mean_im.shape)
    plt.imshow(255-mean_im3, cmap='gray')
    plt.show()
     
    # 90deg rotation anticlockwise
    for i in range(0,mean_im_orig.shape[0],1) :
        for j in range(0,mean_im_orig.shape[1],1) :
            mean_im2[j,i] = mean_im_orig[i,j]
    for i in range(0,mean_im_orig.shape[0],1) :
        for j in range(0,mean_im_orig.shape[1],1) :
            mean_im3[mean_im_orig.shape[0]-1-i,j] = mean_im2[i,j]
#     print(mean_im.shape)
    plt.imshow(255-mean_im3, cmap='gray')
    plt.show()

dt = datetime.now() - t0

print( ' Image rotation with for loop -> elapsed execution time: %0.4f seconds.' %(dt.total_seconds()) )
