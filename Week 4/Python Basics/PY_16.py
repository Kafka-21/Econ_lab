# Instead of try/finally to cleanup resources you can use a with statement
with open("/users/quasar/Downloads/Python/myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file
contents = {"aa" : 12, "bb" : 21}
with open("/users/quasar/Downloads/Python/myfile1.txt", "w+") as file:
    file.write(str(contents)) # writes a string to a file

with open("/users/quasar/Downloads/Python/myfile2.txt", "w+") as file:
    file.write(json.dumps(contents)) # writes an object to a file

# Reading from a file
with open('/users/quasar/Downloads/Python/myfile1.txt', "r+") as file:
    contents = file.read() # reads a string from a file
print(contents) # print : {"aa": 12, "bb" : 21}