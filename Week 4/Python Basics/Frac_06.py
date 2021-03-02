# to print all strong numbers in given lis t

def fact(n):
	return 1 if (n==1 or n==0) else n * fact(n-1)

def is_strongnum(num):
	sum = 0
	n = num
	while n != 0:
		sum += fact(n%10)
		n = n // 10
	if sum == num:
		print(num," is strong number")
	else: 
		print(num," is not strong number")

is_strongnum(145) 

def factorial(number):
	if number == 0 or number == 1:
		fact = 1
	else:
		fact = number * factorial(number - 1)
	return fact

def strong_number(list):
	new_list = []
	for x in list:
		temp = x
		sum = 0
		while temp: 
			rem = temp%10
			sum += factorial(rem)
			temp = temp//10
		if(sum == x):
			new_list.append(x)
		else:
			pass
	return new_list

val_list = [1, 2, 5, 145, 654, 34]
strong_number_list = strong_number(val_list)
print(strong_number_list)
