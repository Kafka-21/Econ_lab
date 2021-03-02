"""
from itertools import product

K, M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

"""

"""
N = []
for _ in range(k):
	# get input and split into list 
	l = input().split()
	# turn list of strings into list of integers
	l = list(map(int,l))
	# Remove index [0] using a slice
	l = l[1:]
	# build list of lists
	N.append(l)
"""

from itertools import product

a = [1, 2]
b = [4, 5]
c = ["x", "y", "z"]
print(*product(a, b, c))
