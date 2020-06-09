import numpy as np


# zero and ones matrices:
a = np.array([1,2,3])
print(a)

z = np.zeros(10)
print(z)

z = np.zeros((10, 10))
print(z)

o = np.ones((10,10))
print(o)


# random generation
r = np.random.rand()  # default is one number if not specified
print(r)


r = np.random.rand(10)
print(r)
r = np.random.random(10)  # equivalent to above
print(r)


r = np.random.randn(10)
print(r)


r = np.random.rand(10,10)
print(r)
r = np.random.random((10,10))  # equivalent to above
print(r)


r = np.random.randn(10,10)
print(r)


# statistics
m = r.mean()
print(m)

v = r.var()
print(v)
    
    



