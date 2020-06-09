import numpy as np

## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""


## Dot product of vectors!

a = np.array([1,2])

b = np.array([2,1])


# method 1
dot = 0.0
for e, f in zip(a,b):
    dot += e*f
    
print(dot)

# method 2
dot2 = a*b
dot2 = np.sum(dot2)
print(dot2)

# method 3
dot3 = (a*b).sum()  ## this is because the function is an instance method of the array itself!
print(dot3)

# method 4
dot4 = np.dot(a,b)
print(dot4)

# method 5
dot5 = a.dot(b)
print(dot5)
dot6 = b.dot(a)
print(dot6)


## Vector magnitude

# method 1
amag = np.sqrt( (a**2).sum() )
print(amag)

# method 2
amag2 = np.linalg.norm(a)
print(amag2)


## cosine of angle

# method 1
cos = a.dot(b) / ( np.linalg.norm(a) * np.linalg.norm(b) )
angle = np.arccos(cos)*180/np.pi    
print(angle)

