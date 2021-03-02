import numpy as np
import math

def basic_sigmoid(x):
	sigm = 1/(1+ math.exp(-x))
	return sigm

x = 0
print(basic_sigmoid(x))


# deep learning uses matrices rather than real number hence use numpy
x = np.array([1,2,3])
# print(np.exp(x))

# vector operation on numpy array
x = np.array([1,2,3])
# print(x+3)

