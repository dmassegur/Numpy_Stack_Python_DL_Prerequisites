import numpy as np
from datetime import *


a = np.random.rand(100)
b = np.random.randn(100)
repeat =  100000


def prod(a,b) :
    result = 0.0
    for i,j in zip(a,b):
        result += i*j 
    return result
        
    
# dot product with for loop
starttime = datetime.now()

for k in range(0,repeat,1):
    dpfor = prod(a,b)
    
et1 = datetime.now() - starttime


# dot product with numpy
starttime = datetime.now()

for k in range(0,repeat,1):
    dpnp = np.dot(a,b)
    
et2 = datetime.now() - starttime


print( ' Dot Product with For Loop -> Elapsed execution time: %0.4f seconds.' %(et1.total_seconds()) )
print( ' Dot Product with Numpy func -> Elapsed execution time: %0.4f seconds.' %(et2.total_seconds()) )
print( ' Numpy func is: %0.4f times faster.' %(et1.total_seconds()/et2.total_seconds()) )
