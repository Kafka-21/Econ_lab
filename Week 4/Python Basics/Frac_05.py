# Program to find ugly number 

""" def ugly(n):
	count = 0 
	num = 1
	while(n > count):
		if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0) :
			count += 1
			print("num : ", num, "count : ", count)
		num = num + 1
	return num-1

"""
# function divides a by greatest divisible power of b
def maxDivide(a,b):
	while a % b == 0:
		a = a / b
		# print("a: ",a)
	return a

# function to check if a number is ugly or not 
def isUgly(no):
	no = maxDivide(no, 2)
	# print("2 no: ",no)
	no = maxDivide(no, 3)
	# print("3 no: ",no)
	no = maxDivide(no, 5)
	# print("5 no: ",no)
	return 1 if no == 1 else 0

# print(isUgly(8))

# Function to get the nth ugly number 
def getNthUglyNo(n):
	i = 1
	count = 1
	# check for all integer untill ugly count becomes n
	while n > count:
		i += 1
		if isUgly(i):
			count += 1
	return i

# driver code to test above functions 
no = getNthUglyNo(150)
print("150th Ugly num : ", no)

# Dynamic programming to get nth ugly number 
def getnthUglyNo(n):
	# to store ugly number 
	ugly = [0] * n
	# 1 is the first ugly number 
	ugly[0] = 1
	# i2, i3, i5 will indicate indices for 2,3,5 respectively 
	i2 = i3 = i5 = 0
	# set initial multiple value
	next_multiple_of_2 = 2
	next_multiple_of_3 = 3
	next_multiple_of_5 = 5
	# start loop to find value from ugly[1] to ugly[n]
	for l in range(1, n):
		# choose the min value of all availabe multiples 
		ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
		# increment the value of index accordingly
		if ugly[l] == next_multiple_of_2:
			i2 += 1
			next_multiple_of_2 = ugly[i2] * 2
		
		if ugly[l] == next_multiple_of_3:
			i3 += 1
			next_multiple_of_3 = ugly[i3] * 3
		if ugly[l] == next_multiple_of_5:
			i5 += 1
			next_multiple_of_5 = ugly[i5] * 5
	return ugly[-1]

print(getnthUglyNo(7))
			





















