# python has print function
print("I'm Python. Nice to meet you!")

# by default the print function also prints out a newline at the end.
# use the optional argument end to change the end string
print("Hello, World", end = "!")

# Simple way to get input data from console
# input_string_var = input("Enter some data:") # Returns the data as a string

# there are no declaration, only assignments
# convention is to use lower_case_with_underscores
some_var = 5
print("\n",some_var)

# accessing a previously unassinged variable is an exception

# if can be used as an expression
# equivalent of C's '?:' ternary operator
print("yahoo!" if 3 > 2 else 2)

# Lists store sequences
li =[]
# Yoy can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1) # li is now [1]
li.append(2) # li is now [1, 2]
li.append(4) # li is now [1, 2, 4]
li.append(3) # li is now [1, 2, 4, 3]
print(li)
# remove from the end with pop
li.pop()
print(li)
# put it back
li.append(3)
# Access a list like you would any array
print(li[0])
print(li[-1])

# you can look at ranges with slice syntax
# start index is included, the end index is not
# (It's a closed/ open range )
print(li[1:3]) # return list from index 1 to 3
print(li[2:])  # return list starting from index 2
print(li[:3])  # return list from beginning until index 3
print(li[::2]) # retunr list selecting every second entry
print(li[::-1]) # return list in reverse order
# use any combination of these to make advanced slices
# li[start:end:step]

# make a one layer deep copy using slices
li2 = li[:] # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false

# remove arbitrary elements from a list with "del"
del li[2]

# remove first occurrence of a value
li.remove(2) # li is now [1, 3]
print(li)
# li.remove(2) # raises a valueerror as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2) # li is now [1, 2, 3] again
print(li)

# get the index of the first item found matching the argument
print(li.index(1))
# li.index(4)

# you can add Lists
# Note : values for li and for other_li are not modified
print(li + other_li)

# concatenate lists with extend()
li.extend(other_li)
print(li)

# Check for existence in a list with "in"
print(1 in li)

# Examine the length with "len()"
print(len(li))

# Tuples are like lists but are immutable
tup = (1, 2, 3)
print(tup[0])
# tup[0] = 3 # raises a type error

# Note that a tuple of length one has to have a comma after the last element but tuples of other lengths even zero, donot
print(type(1))
print(type(1,)) # tuple
# print(type())

# you can do most of the list operations on tuples too
print(len(tup))
print(tup + (4, 5, 6))
print(tup[:2])
print(2 in tup)

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3) # a is now 1, b is now 2 and c is now 3
# you can also do extended unpacking
a, *b, c = (1, 2, 3, 4) # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6 # tuple 4, 5, 6 is unpacked into variables d, e and f respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two next_state_values
e, d = d, e # d is now 5 and e is now 4

# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that the key can be converted to a constant hash value for quick look-ups
# immutable types includes ints, floats, strings, tuples
# invalid_dict = {[1, 2, 3]: "123"} # -> raises a typeError : unhashable type: 'list'
valid_dict = {(1, 2, 3):[1, 2, 3]} # values can be of any type, however

# look up values with []
print(filled_dict["one"]) # => 1

# get all keys as an iterable with "keys()". We need to wrap the call in list() to turn it into a list.
print(list(filled_dict.keys()))
print(list(filled_dict.keys())) # output may change as per version of python

# looking up a non-existing key is a KeyError
# print(filled_dict["four"]) # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one") # => 1
filled_dict.get("four") # => four
# the get method supports a default argument when the value is missing
filled_dict.get("one", 4) # => 1
filled_dict.get("four", 4) # => 4

# "setdefault()" inserts into a dictionary only if the given key is not present
filled_dict.setdefault("five", 5) # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6) # filled_dict["five"] is still 5

# adding to a dictionary
filled_dict.update({"four" : 4 }) # => {"one" : 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4 # another way to add to dict

# check for existence of keys in a dictionary with "in"
print("one" in filled_dict)
print( 1 in filled_dict)

# remove keys from a dictionary with del
del filled_dict["one"] # removes the key "one" from filled dict

# additional unpacking options
{'a' : 1, **{'b' : 2}} # => {'a' : 1, 'b' : 2}
{'a' : 1, **{'a' : 2}} # => {'a' : 2}

# sets store ... well sets
empty_set = set()
# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}

# similar to keys of a dictionary, elements of a set have to be immutable
# invalid_set = {[1], 1} # => raises a type Error: unhashable type : 'list'
valid_set = {(1,), 1}

# add one more item to the set
filled_set = some_set
filled_set.add(5) # filled_set is now {1, 2, 3, 4, 5}
# sets do not have duplicate elements
filled_set.add(5) # it remains as before {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
print(filled_set & other_set)

# Do set union with
print(filled_set | other_set)

# Do set difference with -
print({1, 2, 3, 4} - {2, 3, 5}) # => {1, 4}

# do set symmetric difference with ^
print({1, 2, 3, 4} ^ {2, 3, 5})

# check if set on the left is a superset of set on the right
print({1,2} >= {1, 2, 3})

# check if set on the left is a subset of set on the right
print({1,2} <= {1, 2, 3})

# check for existence in a set with in
print(2 in filled_set)
print(10 in filled_set)

# Make a one layer deep copy
filled_set = some_set.copy # filled_set is {1, 2, 3, 4, 5}
print(filled_set is some_set) # => False


# Loop operations
some_var = 5

if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10: # this elif clause is optional
    print("some_var is smaller than 10")
else:
    print("some var is indeed 10.")

""" For looprs iterate overs lists print
dog is a mammal
cat is a mammal
mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # you can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers from zero to the given number prints:
0
1
2
3
"""

for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers from lower number to the upper number prints:
4
5
6
7
"""
print("\n")

for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers from the lower number to the upper number, while incrementing by step.
If step is not indicated, the default value is 1. prints
4
6
"""
for i in range(4, 8, 2):
    print(i)

"""
To loop over a list, and retreieve both the index and the value of each item is the list.
prints:
0 dog
1 cat
2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

"""
While loops go until a condition is no longer met.
prints:
0
1
2
3
"""
x = 0
while x < 4:
    print(x)
    x += 1

# Handle exceptions with a try/except block
try:
    # use "raise" to raise an Error
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here
except (TypeError, NameError):
    pass # Multiple exceptions can be handled together if required
else:
    #optional caluse to the try/except block. Must follow all except blocks
    print("All good!") # runs only if the code is try raises no exceptions
finally:
    # Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("/users/quasar/Downloads/Python/myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file
contents = {"aa" : 12, "bb" : 21}
with open("/users/quasar/Downloads/Python/myfile1.txt", "w+") as file:
    file.write(str(contents)) # writes a string to a file

# with open("/users/quasar/Downloads/Python/myfile2.txt", "w+") as file:
#    file.write(json.dumps(contents)) # writes an object to a file

# Reading from a file
with open('/users/quasar/Downloads/Python/myfile1.txt', "r+") as file:
    contents = file.read() # reads a string from a file
print(contents) # print : {"aa": 12, "bb" : 21}

# python offers a fundamental abstraction called the Iterable. An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable
filled_dict = {"one" : 1, "two" : 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three']). this is an object that implements our iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i) #prints one, two, three

# However we cannot address elements by index
# out_iterable[1] # Raises a TypeError

# An iterable is an object that knows how to create an iterator
our_iterator = iter(our_iterable)
print(next(our_iterator)) # prints one
# our iterator is an object that can remember the state as we transverse through it.
# We get the next object with "next()"
for i in our_iterator:
    print(i)  # prints two, three
# you can grab all the elements of an iterable or iterator by calling list() on it
print(list(our_iterable))
print(list(our_iterator)) # returns [] because state is saved

# use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x,y))
    return x + y # return values with a return statement

add(5, 6)
add(y=6, x=5) # Keyword arguments can arrive in any order

# You can define functions that take a variable number of positional arguments
def varargs(*args):
    return args

print(varargs(1,2,3))

# You can define functions that take a variable number of keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
print(keyword_args(big = "foot", loch ="ness"))

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b" : 4}
print(all_the_args(*args))
print(all_the_args(**kwargs))
print(all_the_args(*args, **kwargs))

# Returning Multiple values (with tuple assignments)
def swap(x, y):
    return y, x
# return Multiple values as a tuple wthout the parentheses.
# Note: parentheses have been excluded but can be included

x = 1
y = 2
x, y = swap(x, y) # => x = 2, y = 1

# Function scope
x = 5
def set_x(num):
    # local var x not the same as global variable x
    x = num
    print(x)

def set_global_x(num):
    global x
    print(x)
    x = num # global var x is now set to 6
    print(x)

set_x(43)
set_global_x(6)

# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3))

# there are also anonymous functions
print((lambda x: x > 2)(3))
print((lambda x, y:x**2 + y**2)(2, 1))

# There are built in higher order functions
print(list(map(add_10, [1, 2, 3])))
print(list(map(max,[1, 2, 3], [4, 2, 1])))
print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
print([add_10(i) for i in [1, 2, 3]])
print([x for x in [3, 4, 5, 6, 7] if x > 5])

# you can construct set and dict comprehensions as well
print({x for x in 'abcddeef' if x not in 'abc'})
print({x: x**2 for x in range(5)})

# imort modules
import math
print(math.sqrt(16))

# You can get specific function from a module
from math import ceil, floor
print(ceil(3.7))
print(floor(3.7))

# You can import all funtions from a modules
# Warning : this is not recommended
# from math import *

# you can shorten module names
import math as m
print(math.sqrt(16) == m.sqrt(16))

# Python modules are just ordinary Python files.

# classes
class Human:
    # A class attribute. It is shared by all instance of this class
    species = "H. Sapiens"
    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects or attributes that are used by Python but that live in user-controlled names
    # methods like : __init__, __str__, __repr__ etc. are called special methods (or sometimes called dunder methods)
    # you should not invent such names on your own
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name
        # Initialize property
        self._age = 0
    # an instance method. All method take "self" as the first arguments
    def say(self, msg):
        print("{name} : {message}".format(name = self.name, message = msg))
    # Another instance method
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'
    # A class method is shared among all instances. They are callled with calling class as first argument
    @classmethod
    def get_species(cls):
        return cls.species
    # A static method is called without a class or instance reference
    def grunt():
        return "*grunt"
    # A property is just like a getter.
    # It turns the method age() into an read only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though
    @property
    def age(self):
        return self._age
    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age
    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

# When a python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this moduel is the main program
if __name__ == '__main__':
    # Instantiate a class
    i = Human(name = "Ian")
    i.say("hi")
    j = Human("Joel")
    j.say("Hello")
    # i and j are instances of type human, or in other words: they are Human objects
    # call our class methods
    i.say(i.get_species())
    # change the shared attribute
    Human.species = "H.neanderthalensis"
    i.say(i.get_species())
    j.say(j.get_species())
    # call the static method
    print(Human.grunt())
    # cannot call static method with instance of object because i.grunt() will automatically put "self" (the object i) as an argument
    # print(i.grunt()) # TypeError : grunt() takes 0 positional arguments but 1 was given
    # update the property for this instance
    i.age = 42
    # get the property
    i.say(i.age)
    j.say(j.age)
    # delete the property
    del i.age

# Inheritance - allows new child classes to be defined that inherit methods and variables from their parent class
"""
Using the human class defined above as the base or parent class, we can define a child class, Superhero
which inherits the class variables like "species", "name" and "age" as well as methods, like "sing" and "grunt"
from the human class, but can also have its own unique properties.

 To take advantage of modularization by file you could place classes above in their own files say, human.py
"""

# generators help you make lazy code
def double_numbers(iterable):
    for i in iterable:
        yield i + i
"""
Generators are memory-efficient because they only load the data needed to process the next value in iterable.
This allows them to perform operations on otherwise prohibitively large value ranges.
"""
for i in double_numbers(range(1, 900000000)):
    # range is a generator
    print(i)
    if i >= 30:
        break

# Just as you can create a list comprehension, you can create generator comprehension as well
values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x)

# You can also cast a generator comprehension directly to a list
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)

# Decorators
# In this example 'beg' wraps 'say'. If say_please is true then it will change the returned message
from functools import wraps

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg
    return wrapper

@beg
def say(say_please = False):
    msg = "Can you buy me a beer?"
    return msg, say_please

print(say())
print(say(say_please = True))

# zipping and unzipping lists and iterables
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = zip(a,b)
print(list(z))
print(list(zip(*z)))

# grouping adjacent list items using zip

a = [1, 2, 3, 4, 5, 6]
# using iterators
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
print(list(group_adjacent(a, 3)))
print(list(group_adjacent(a, 2)))

# Using slices
from itertools import islice
group_adjacent = lambda a, k: zip(*(islice(a, i, None, k) for i in range(k)))
print(list(group_adjacent(a, 3)))
print(list(group_adjacent(a, 2)))
print(list(group_adjacent(a, 1)))

# Sliding windows (n-grams) using zip and iterators
def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)

a = [1, 2, 3, 4, 5, 6]
print(list(n_grams(a, 3)))
print(list(n_grams(a, 2)))
print(list(n_grams(a, 4)))

# inverting a dictionary using zip
m = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
print(m.items())
print(list(zip(m.values(), m.keys())))
mi = dict(zip(m.values(), m.keys()))
print(mi)

# Flattening Lists
import itertools
a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)))
print(sum(a, []))
print([x for l in a for x in l])
a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print([x for l1 in a for l2 in l1 for x in l2])
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else[x]
print(flatten(a))

# Generator expression
g = (x**2 for x in range(10))
print(next(g))
print(next(g))
print(sum(x**3 for x in range(10)))
print(sum(x**3 for x in range(10) if x%3 == 1))

# Dictionary comprehension
m = {x : x**2 for x in range(5)}
print(m)
m = {x : 'A' + str(x) for x in range(10)}
print(m)

# inverting a dictionary using a dictionary comprehension
m = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
print(m)
print({v : k for k, v in m.items()})

# Named tuples(collections.namedtuple)
import collections
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x = 1.0 , y = 2.0)
print(p)

# Inheriting from named tuples
class Point(collections.namedtuple('PointBase', ['x', 'y'])):
    __slot__ = ()
    def __add__(self, other):
        return Point(x = self.x + other.x, y = self.y + other.y)

p = Point(x = 1.0, y = 2.0)
q = Point(x = 2.0, y = 3.0)
print(p+q)

# sets and set operations 
A = {1, 2, 3, 3}
print(A)
B = {3, 4, 5, 6, 7}
print(B)
print(A|B)
print(A&B)
print(A-B)
print(B-A)
print(A^B)
print((A^B) == ((A-B) |(B-A)))

# Multisets and multiset operations(collections.Counter)
A = collections.Counter([1, 2, 2])
B = collections.Counter([2, 2, 3])
print(A)
print(B)
print(A|B)
print(A&B)
print(A+B)
print(A-B)
print(B-A)


# Most common elements in an iterable(collections.Counter)
A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print(A)
print(A.most_common(1))
print(A.most_common(3))

# Double-ended queue(collections.deque)
Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
print(Q)
print(Q.pop())
print(Q.popleft())
print(Q)
print(Q.rotate(-3))

# double-ended queue with maximum length(collections.deque)
last_three = collections.deque(maxlen = 3)
for i in range(10):
    last_three.append(i)
    print(','.join(str(x) for x in last_three))

# Ordered dictionaries (collections.OrderedDict)
m = dict((str(x), x) for x in range(10))
print(', '.join(m.keys()))
m = collections.OrderedDict((str(x), x) for x in range(10))
print(', '.join(m.keys()))
m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
print(', '.join(m.keys()))


# Mapping objects to unique conunting numbers(collections.defaultdict)
"""
import itertools, collections
value_to_numeric_map = collections.defaultdict(itertools.count().next)
print(value_to_numeric_map['a'])
print(value_to_numeric_map['b'])
print(value_to_numeric_map['c'])
print(value_to_numeric_map['d'])
"""

import random, heapq

# Largest and smallest elements(heapq.nlargest and heapq.nsmallest)
a = [random.randint(0, 100) for _ in range(100)]
print(heapq.nsmallest(5,a))
print(heapq.nlargest(5, a))

# Cartesian products(itertools.product)
for p in itertools.product([1, 2, 3], [4, 5]):
    (1, 4)
    (1, 5)
    (2, 4)
    (2, 5)
    (3, 4)
    (3, 5)

for p in itertools.product([0, 1] , repeat = 4):
    print(''.join(str(x) for x in p))

# Combinations and combinations with replacement(itertools.combinations and itertools.combinations_with_replacement)
for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print(''.join(str(x) for x in c))

for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(''.join(str(x) for x in c))

# permutations(itertools.permutations)
for p in itertools.permutations([1, 2, 3, 4]):
    print(''.join(str(x) for x in p))

# Chaining iterables(itertools.chain)

a = [1, 2, 3, 4]
for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
    print(p)















































































