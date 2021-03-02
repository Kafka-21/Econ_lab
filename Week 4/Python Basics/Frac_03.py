def gcd(x, y):
	if x > y:
		smaller = y
	else:
		smaller = x
	for i in range(1, smaller+1):
		if((x % i == 0) and (y % i == 0)):
			hcf = i
	return hcf
	
# HCF using eulidean algorith = fact that HCF of 2 numbers divide their difference as well 
""" in this algorithm we divide the greater by smaller and take the remainder, now divide the smaller by this 
remainder. Repeat until the remainder is 0 """

def find_gcd(x, y):
	while(y):
		x, y = y, x%y
	return x

l = [2, 4, 6, 8, 16]

num1 = l[1]
num2 = l[4]
print(num1, num2, find_gcd(num1, num2))
print(num1, num2, gcd(num1, num2))

"""
for i in range(2, len(l)):
	gcd = find_gcd(gcd, l[i])

print(gcd)"""