import numpy as np

arr = np.array([1, 3, 2, 4, 5])
print(arr.argsort()[-3:][::-1])

a = np.array([1,2,3,4,5])
p = np.percentile(a, 50) #Returns 50th percentile, e.g. median
print(p)

# num1 = int(input())
# num2 = int(input())
num1 = 10
num2 = 20
print(int(num1/num2))
print(float(num1/num2))

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            return False
        return True
    else:
        return leap

# year = int(input())
# print(is_leap(year))

# for printing consecutive number 
n = 10
print(*range(1, n+1), sep='')

