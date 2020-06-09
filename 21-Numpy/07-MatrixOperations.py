import numpy as np


A = np.round( np.random.rand(2,2)*10 )
A = np.array([[1,2], [3,4]])
print('A:\n', A)


# Inverse
Ainv = np.linalg.inv(A)
print('inverse of A:\n', Ainv)


I = np.dot(A,Ainv)
print('A dot A^-1 = I:\n', I)

I = np.dot(Ainv,A)
print('A^-1 dot A = I:\n', I)


# Determinant
Det = np.linalg.det(A)
print('Det(A):\n', Det)


# Diagonal
diag = np.diag(A)
print('diagonal terms of matrix A:\n', diag)

diag = np.diag([1,2])
print('diagonal matrix from array:\n', diag)



a = np.array([1,2])
b = np.array([3,4])

# Inner product = dot product
dp = np.dot(a,b)
print('Dot product of a and b:\n', dp)
ip = np.inner(a,b)
print('Inner product (same as dot product) of a and b:\n', ip)


# Outer product: Ai.Bj
op = np.outer(a,b)
print('Outer product of a and b:\n', op)


# Sum of the diagonals
diagsum = np.diag(A).sum()
print('Sum of diagonal terms of A:\n', diagsum)
diagsum = np.trace(A)
print('Sum of diagonal function of A:\n', diagsum)


# Covariance
X = np.random.rand(5,3)
print('X:\n',X)

cov = np.cov(X)
print('Covariance of X:\n',cov)  # creates a mxm covariance matrix

covt = np.cov(X.T)
print('Covariance of X\':\n',covt)  # creates a nxn covariance matrix


# Eigenvalues and Eigenvectors:
[eigval, eigvec] = np.linalg.eig(covt)
print('Eigenvalues of the covariance transpose:\n',eigval)
print('Eigenvectors of the covariance transpose:\n',eigvec)

# Hermitian Eigenvalues and Eigenvectors:
[eighval, eighvec] = np.linalg.eigh(covt)
print('Hermitian Eigenvalues of the covariance transpose:\n',eighval)
print('Hermitian Eigenvectors of the covariance transpose:\n',eighvec)


