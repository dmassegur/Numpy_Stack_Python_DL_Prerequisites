import numpy as np
import matplotlib.pyplot as plt


## Ex1: compute v = A*v many times to show that it is an eigenvector


A = np.array([[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]])

print(A.shape)

v = np.array([np.random.rand(1), np.random.rand(1)])
# v = np.array([1/3, 1/3])
sum = v.sum()
print('v components: [ %0.4f, %0.4f ]. sum: %0.4f.'  %(v[0], v[1], sum))

# adding the 1 - sum of the first two components as a third element so that the total sum is = 1.
v = np.append(v, 1-sum)
print(v.shape)
print('v components:', v,' -> sum: %0.4f.'  %(np.sum(v)))


print('')

iter = 100
dist = np.array([])
for i in range(0,iter,1) :
    
    v2 = np.dot(A, v.T)
    v2 = v2.T
    
    # euclidean distance:
    dist = np.append(dist, np.linalg.norm(v2-v))
    v = v2
    print(v)


plt.plot(range(1,iter+1,1), dist, label='euclidean dist')
plt.xlabel('iteration i')
plt.ylabel('euclidean distance v*A^i')
plt.title('euclidean distance evolution for v=v*A^i')
plt.axis([1, iter, 0, np.max(dist)])
plt.grid()
plt.legend()
plt.show()

print('Final v components:', v,' -> sum: %0.4f.'  %(np.sum(v)))
print('Product A*v:', np.dot(A, v.T))
print('Product 1*v:', 1*v.T)
print('A*v = 1*v -> v is an eigenvector of A with eigenvalue 1!!!')


print('')

# Eigenvalues and Eigenvectors:
[eigval, eigvec] = np.linalg.eig(A)
print('Eigenvalues of matrix A:\n',eigval)
print('Eigenvectors of matrix A:\n',eigvec)
print('Product A*eigvect1:', np.dot(A,eigvec[:,0]))
print('Product eigval1*eigvect1:', eigval[0]*eigvec[:,0])




