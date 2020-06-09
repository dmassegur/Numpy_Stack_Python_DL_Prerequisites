import numpy as np
from datetime import datetime 

A = np.array([[1,2], [3,4]])
b = np.array([3,4])
print('A:\n', A)
print('b:\n', b)

repeat = 10000


## Resolving linear system by inverting A:
t0 = datetime.now()

for i in range(0,repeat,1) :
    # A-1 * b
    Ainv = np.linalg.inv(A)
    x = np.dot(Ainv,b)
    print('Ax=b Linear System solution inverting A -> x=A^-1dotb\n',x)

dt1 = datetime.now() - t0


## Resolving linear system using solve():
t0 = datetime.now()

for i in range(0,repeat,1) :
    # Using a function
    x = np.linalg.solve(A,b)
    print('Ax=b Linear System solution using solve() -> x=solve(A,b):\n',x)

dt2 = datetime.now() - t0


print('Time to resolve linear system by inverting:',dt1.total_seconds())
print('Time to resolve linear system using solve():',dt2.total_seconds())
print( 'Numpy solve() is: %0.4f times faster.' %(dt1.total_seconds()/dt2.total_seconds()) )
