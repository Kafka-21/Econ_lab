# print fibonacci numbers

def fibonacci_rec(n):
	if n < 0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n == 1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(9))

# using Dynamic Programming 
FibArray = [0,1]

def fibonacci_dyn(n):
	if n<0:
		print("Incorrect input")
	elif n <= len(FibArray):
		return FibArray[n-1]
	else: 
		temp_fib = fibonacci_dyn(n-1) + fibonacci_dyn(n-2)
		FibArray.append(temp_fib)
		return temp_fib

print(fibonacci_dyn(10))

# space optimisation 
def fibonacci_spa(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2,n):
			c = a + b
			a = b
			b = c
		return b 
print(fibonacci_spa(10))
