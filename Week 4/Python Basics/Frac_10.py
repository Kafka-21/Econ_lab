def pyfunc(r):
	for x in range(r):
		print(' '*(r-x-1)+'*'*(2*x+1))

pyfunc(5)


# prime number checking 
num = 21
for x in range(2, num):
	if num%x == 0:
		print("Not Prime")
		break
	else:
		print("Prime")


# Palindrome 
a = 'nitin'
b = a[::-1]
if a == b:
	print("Palindrome")
else:
	print("Not Palindrome")

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

