# map function returns a map object(which is an itertor) of the results after applying the given function of each item of a given iterable

def addition(n):
	return n + n

numbers = (1,2,3,4)
result = map(addition, numbers)
print(list(result))

# using lambda function to do some task 
result = map(lambda x: x+x, numbers)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list,l))
# print(test)

from itertools import product

print(list(product([1, 2, 3], repeat = 2)))
print(list(product([1, 2, 3], [3, 4])))
A = [[1, 2, 3], [3, 4, 5]]
print(list(product(*A)))
B = [[1, 2, 3], [3, 4, 5], [7, 8]]
print(list(product(*B)))

print(list(map(len, ['Tina', 'Raj', 'Tom'])))
sum = lambda a,b,c : a + b + c
print(sum(1,2,3))

