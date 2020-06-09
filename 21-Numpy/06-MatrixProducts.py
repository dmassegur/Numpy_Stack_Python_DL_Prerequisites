import numpy as np


A = np.round( np.random.rand(2,2)*10 )
B = np.round( np.random.rand(2,2)*10 )
print('A:\n', A)
print('B:\n', B)


### Element multiplication!!!
P = A*B
print('Elementwise product:\n',P)


### Dot multiplication!!!
PP = np.dot(A,B)
print('Dot product:\n',PP)
