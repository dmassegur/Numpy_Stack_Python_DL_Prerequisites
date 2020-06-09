import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import *


## Ex5: Write a function that tests whether a matrix is symmetric or not


# checking matrix symmetry with for loop
def SymMatrixForLoop(M):
    m = M.shape[0]
    n = M.shape[1]
    result = True
    
    for i in range(0,m,1) :
        for j in range(0,n,1) :
            if M[i,j] == M[j,i] :
                result = True
            else :
                result = False
                break
    return result


# checking matrix symmetry with transpose
def SymMatrix(M, tol=1e-8):
#     result = False
#     if np.all( np.abs(M-M.T) < tol ) :
#         result = True
# 
#     return result

    # alternative
    return np.all( np.abs(M-M.T) < tol ) 



iterations = 10000

print('')
print('Checking Matrix symmetry with transpose function...')

t0 = datetime.now()
for i in range(0,iterations,1) :
    A = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
    print('Matrix A =\n',A)
    
    symcheck = SymMatrix(A)       
    if symcheck :
        print('Matrix A is symmetric')
    else :
        print('Matrix A is assymmetric')
        
    print('')    
    B = np.array([ [1, 2, 3], [2, 5, 6], [3, 6, 9] ])
    print('Matrix B =\n',B)
    
    symcheck = SymMatrix(B)       
    if symcheck :
        print('Matrix B is symmetric')
    else :
        print('Matrix B is assymmetric')
    
dt1 = datetime.now() - t0




print('')
print('Checking Matrix symmetry with for loop function...')

t0 = datetime.now()

for i in range(0,iterations,1) :
    A = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
    print('Matrix A =\n',A)
    
    symcheck = SymMatrixForLoop(A)       
    if symcheck :
        print('Matrix A is symmetric')
    else :
        print('Matrix A is assymmetric')
        
    print('')    
    B = np.array([ [1, 2, 3], [2, 5, 6], [3, 6, 9] ])
    print('Matrix B =\n',B)
    
    symcheck = SymMatrixForLoop(B)       
    if symcheck :
        print('Matrix B is symmetric')
    else :
        print('Matrix B is assymmetric')
    
dt2 = datetime.now() - t0



print('')
print( 'Matrix symmetry check with transpose %d times, elapsed time: %0.4f seconds.' %(iterations,dt1.total_seconds()) )
print('')
print( 'Matrix symmetry check with for loop %d, elapsed time: %0.4f seconds.' %(iterations,dt2.total_seconds()) )
