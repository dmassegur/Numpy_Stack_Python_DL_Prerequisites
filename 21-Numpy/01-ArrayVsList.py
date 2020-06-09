import numpy as np
import sys

## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""


# python version
print(sys.version)


l = [1,2,3,4,5]
print(l)

a = np.array([1,2,3,4,5])
print(a)

for i in l:
    print(i)

for i in a:
    print(i)


l.append(6)
print(l)

#a.append(6)  #doesn't work
#print(a)


l += [7]

#a += [6, 7]  #doesn't work


## sum of elements

# with list the + does concatenation not sum! so we have to do a loop
l2 = []
for e in l:
    l2.append(e+e)
    
print(l2)

# with array:
b = a+a
print(b)

## converting list into array:
a2 = np.array(l)


## multiplication
l2 = 2*l
b = 2*a
print(b)


## square
#l2 = l**2  # doesnt' work
l2 = []
for i in l:
    l2.append(i*i)
    
print(l2)

b = a**2
print(b)


sq = np.sqrt(a)
print(sq)

lg = np.log(a)
print(lg)

ex = np.exp(a)
print(ex)

