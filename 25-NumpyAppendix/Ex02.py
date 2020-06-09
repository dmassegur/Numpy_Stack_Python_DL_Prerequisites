import numpy as np
import matplotlib.pyplot as plt


## Ex2: sum of 1000 random numbers repeated 1000 times to prove that it follows a normal distribution


# tests
a = np.array([1, 2, 3]) # this is not an array of arrays! it's only an array!
print(a.shape)
at = a.T
print(at.shape)
a = np.append(a, a, axis=0)
print(a.shape)

print('')
a = np.array([[1, 2, 3]]) # this is an array of arrays! 2D array
print(a.shape)
at = a.T
print(at.shape)
a = np.append(a, a, axis=0)
print(a.shape)

print('')
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
at = a.T
print(at.shape)
a = np.append(a, a, axis=0)
print(a.shape)


# exercise begins
print('')
m = 1000
n = 1000
# Y = np.array([[]])
# print(Y.shape)
for i in range(0,m,1) :
    # x = np.random.rand(n)  # this is not an array of arrays! it's only an array!
    x = np.array([np.random.rand(n)])  # this is an array of arrays! 2D array
#     print(x.shape)
    if i==0 :
      Y = x   # initializing Y with first row of x
    else :
      Y = np.append(Y, x, axis=0)  # appending the following x rows
    
#     print(Y.shape)
    x_sum = np.sum(x)

print('Y dimensions:', Y.shape)  

print('Sum on each row of matrix Y: ...')
# summing the column values for each row
Y_xsum = np.sum(Y, axis=0)
print('Summed columns for each row -> dimensions:', Y_xsum.shape)


print('')
# plotting histogram of Y -> should be a gaussian distribution
plt.hist(Y_xsum, bins=100)
plt.xlabel('Y value')
plt.ylabel('frequency')
plt.grid()
plt.show()

# plotting histogram of last row of Y -> each row should be a normal distribution
plt.hist(Y[Y.shape[0]-1,:], bins=100)
plt.xlabel('X value of last example')
plt.ylabel('frequency')
plt.grid()
plt.show()


avg = np.mean(Y_xsum)
std = np.std(Y_xsum)
print('Mean and Variance of Y: mu = %0.3f, var = %0.3f' %(avg, std**2))

  


