import numpy as np

A = np.array( [ [1, 1], [1.50, 4.0] ] )
b = np.array( [2200, 5050])

x = np.linalg.solve(A,b)

print( 'Number of children attended: %d.' %(int(x[0])) )
print( 'Number of adults attended: %d.' %(int(x[1])) )