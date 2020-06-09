import numpy as np


## Matrix definition

# numpy array of arrays
M = np.array([ [1,2], [3,4] ])

# dimensions of the matrix:
print(M.shape)

# list of lists:
L = [[1,2], [3,4]]

print(M[0])
print(L[0])

print(M[0][0])
print(L[0][0])

print(M[0,0])


# numpy Matrix
M2 = np.matrix([ [1,2], [3,4] ])
print(M2)

# convert Matrix to array
M2a = np.array(M2)
print(M2a)



# Transpose:
Mt = M.T
print(Mt)