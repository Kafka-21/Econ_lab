def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while n > 1:
			fact *= n
			n -= 1
		return fact

def fact(n):
	return 1 if (n==1 or n==0) else n* fact(n-1)

print(factorial(5))
print(fact(4))
