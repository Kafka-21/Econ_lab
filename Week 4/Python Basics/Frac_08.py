""" use __init__ - method or constructor in python. method automatically called to allocate memory when a new object
/instance of a class is created. All classes have the __int__ method """

class Employee:
	def __init__(self, name, age,salary):
		self.name = name
		self.age = age
		self.salary = 20000

E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1. 
print(E1.name)
print(E1.age)
print(E1.salary)

""" Lambda function - an anonymous function is known as a lambda function. This function can have any number of parameters
but, can have just one statement """

a = lambda x,y : x+y
print (a(5,6))

""" self is an instance or an object of a class. In python, this is explicitly included as the first parameter.
It helps to differentiate between the methods and attributes of a class with local variables. The self variable
in the init method refers to the newly created object while in the other methods, it refers to the object whose 
method was called """

"""
Break : allows loop termination when some condition is met and the control is transferred to the next statement

Continue : allows skipping some part of a loop when some specific condition is met and the control is transferred
to the begining of the loop

Pass : used when you need some block of code syntactically, but you want to skip its execution. This is basically
a null operation. Nothing happens when this is executed.
"""

""" [::-1] is used to reverse the order of an array or sequence 
it reprints a reversed copy of ordered data structures such as an array or a list, the original array or list 
remains unchanged. 
"""
import array as arr

My_Array = arr.array('i',[1,2,3,4,5])
print(My_Array[::-1])

""" Randomize the items of a list """
from random import shuffle
x = ['Keep', 'The', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

""" 
Generate random numbers 

import random
random.random

the statement random.random() method return the floating point number that is in the range of [0,1]. The 
The function generates random float numbers. The methods that are used with the random class are the bound methods
of the hidden instances. The instances of the Random can be done to show the multi-threading programs that creates
a different instance of individual threads. The other random generators that are used in this are:

randrange(a,b)
uniform(a,b) 
normalvariabte(mean,sdev)- for normal distribution 
Random class 
"""
# doc string and comments 
# converting in lower case

x = "ABCD"
print(x.lower())

"""
Operators are special functions. They take one or more values and produce a corresponding result.

is: returns true when 2 operands are true  (Example: “a” is ‘a’)

not: returns the inverse of the boolean value

in: checks if some element is present in some sequence
"""


""" 
Dictionary - built in datatypes in python. It defines one-to-one relationship between key and values.
Dictionaries contain pair of keys and their corresponding values. Dictionaries are indexed by keys.
"""
dict = {'Country':'India', 'Capital':'Delhi', 'PM':'Modi'}
print(dict)
print(dict['Country']) 
print(dict['Capital'])
print(dict['PM'])
 
"""
The ternary operator - used to show the conditional statements. This consists of true and false
values with a statement that has to be evaluated for it. """

"""
*args when we aren’t sure how many arguments are going to be passed to a function, or if we want to 
pass a stored list or tuple of arguments to a function. 

**kwargs is used when we don’t know how many keyword arguments will be passed to a function, 
or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args 
and kwargs are a convention, you could also use *bob and **billy but that would not be wise
"""

"""
split() - uses a regex pattern to split a given string into a list 
sub() - finds all substrings where regex pattern matches and then replace them with a different string 
subn() - similar to sub() and also returns the new string along with the no. of replacement 
"""

"""
postive and negative indexes

The index for the negative number starts from ‘-1’ that represents the last index in the sequence 
and ‘-2’ as the penultimate index and the sequence carries forward like the positive number.

The negative index is used to remove any new-line spaces from the string and allow the string to 
except the last character that is given as S[:-1]. The negative index is also used to show the index 
to represent the string in correct order.
"""

"""
Python list operation - insertion, delection, appending and concatenation and Python's list comprehension
certain limitation - no support vectorizied operations like elementwise addition and multiplication
"""

# Python array
a = arr.array('d', [1.1, 2.1, 3.1])
print(a)
a.append(3.4)
print(a)
a.extend([4.5, 6.3, 6.8])
print(a)
a.insert(2,3.8)
print(a)

# pop() - returns deleted value , remove() - no value return 

print(a.pop())
print(a.pop(3))
a.remove(1.1)
print(a)

""" 
Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the 
new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These 
references point to the original objects and the changes made in any member of the class will also affect 
the original copy of it. Shallow copy allows faster execution of the program and it depends on the size of 
the data that is used.

Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers 
to the objects. It makes the reference to an object and the new object that is pointed by some other object 
gets stored. The changes made in the original copy won’t affect any other copy that uses the object. Deep 
copy makes execution of the program slower due to making certain copies for each object that is been called.
"""

# split method for strin g
a = "edureka python"
print(a.split())

# classes in python
class employee:
	def __init__(self, name):
		self.name = name

E1 = employee("abc")
print(E1.name)

# Monkey patching - refers to dynamic modifiction of a class or moduel at run-time 

import m
def monkey_f(self):
	print("monkey_f()")
 
m.MyClass.f = monkey_f
obj = m.MyClass()
obj.f()

# some changes in the behavior of f() in MyClass using the function we defined, monkey_f(), outside of the module m

# create an empty class in python using pass (pass does nothing )
class a:
	pass
obj = a()
obj.name ="xyz"
print("Name : ",obj.name)










