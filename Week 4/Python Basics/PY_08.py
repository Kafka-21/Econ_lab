import numpy as np

# generating 5 gaussian random number  and generate rank 1 array neither row ro column array
a = np.random.randn(5)
# print(a)

# printing size of vector array
# print(a.shape)

#transpose of array
# print(a.T)

# print(np.dot(a,a.T))

# to avoid this problem 1- column vector 
# a = np.random.randn(5,1)
# print(a)
# print(a.T)
# print(np.dot(a,a.T))

# row vector
a = np.random.randn(1,5)
print(a)

# to know dimension of vector
assert(a.shape == (1,5))
# if problem with array then reshape with shape
a = a.reshape((5,1))
print("\n",a)



