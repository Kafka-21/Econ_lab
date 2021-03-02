def even(num):
	if num%2 == 0:
		return True

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(list(filter(even, lst)))

# using lambda rather than function 
print(list(filter(lambda num: num%2 == 0, lst)))

# using map function 
print(list(map(lambda num: num%2 == 0, lst)))

num = 24 
def even_or_odd(num):
	if num%2 == 0:
		print("The number {} is even".format(num))
	else:
		print("The number {} is odd".format(num))

print(even_or_odd(num))

# addition using lambda function 
addition = (lambda a,b: a+b)
print(addition(12,14))

# using map function instead of loop - iteration issue - lazy loading memory 
print(list(map(even_or_odd, lst)))

# List comprehension - append function 
lst1= []
def lst_square(lst):
	for i in lst:
		lst1.append(i*i)
	return lst1

print(lst_square([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# more line of code more memory and for loop - hence list comprehension
lst = [1, 2, 3, 4, 5] # double brackets means multiple nexted list 
print([i*i for i in lst])
# if condition in comprehension list 
print([i*i for i in lst if i%2 == 0]) 

# string formatting in python

# using place holder 
strs = "Hello"

def greeting(name):
	return "Hello {} welome to the community".format(name)

print(greeting("Nitin"))

def welcome_email(firstname, lastname):
	return "Welcome {} {}".format(firstname, lastname)

print(welcome_email("Nitin", "Gautam"))

# using name to placeholder 
def welcome_email1(firstname, lastname):
	return "Welcome {f_name} {l_name}".format(l_name = lastname, f_name = firstname)

print(welcome_email1("Mike", "Ross"))

# Iterables vs iterators

lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
	print (i)

# using iter function - iterables -all values stored in memory while in above not all memory initialized in memory 
lst1 = iter(lst)
# to use iter use next function 
print(next(lst1))
# using for loop for iter 
for i in lst1:
	print(i)






























