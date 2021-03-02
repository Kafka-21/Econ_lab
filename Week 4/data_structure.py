# list in python

# create empty list 
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types 
my_list = [1, "Hello", 3.4]

# nested list 
my_list = ["mouse", [8, 4, 6], ['a']]

# list indexing 
my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[0])
print(my_list[2])

# tuples in python 
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print("Length of tuple :", len(mytuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")  #Not a tuple rather string
print(type(thistuple))


# creating dictionary in python

thisdict = { 
          "brand": "Maruti",
          "model": "Swift",
          "year": 2007
}

print(thisdict)
print(thisdict["brand"])


# converting dictionary to JSON use json.dumps()
import json

person = {
          'Name' : "XYZ",
          'Man' : True,
          'Address' : "Delhi",
          'Education' : "M.Sc. Economics"
}

print(person)
print("Datatype before conversion: ", type(person))
json_string = json.dumps(person)
print(json_string)
print("Datatype after conversion", type(json_string))

# Json file in formatted 
json_string_formatted = json.dumps(person, indent = 4)
print(json_string_formatted)

# saving python objects to a file 
with open("data_file.json", "w") as fp:
          json.dump(person, fp, indent = 4)

# json.load() and json.loads() are methods used to read files and convert JSON to dictionary respectively
with open("data_file.json", "r") as fp : #r - open file in read mode
          data =  json.load(fp)

#print(data) #data is a dict 
