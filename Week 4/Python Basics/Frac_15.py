# Returns value of Permutation 
# Coefficient P(n, k) 
def permutationCoeff1(n, k): 
  
    P = [[0 for i in range(k + 1)]  
            for j in range(n + 1)] 
  
    # Calculate value of Permutation 
    # Coefficient in 
    # bottom up manner 
    for i in range(n + 1): 
        for j in range(min(i, k) + 1): 
  
            # Base cases 
            if (j == 0): 
                P[i][j] = 1
  
            # Calculate value using  
            # previously stored values 
            else: 
                P[i][j] = P[i - 1][j] + ( 
                           j * P[i - 1][j - 1]) 
  
            # This step is important  
            # as P(i, j) = 0 for j>i 
            if (j < k): 
                P[i][j + 1] = 0
    return P[n][k] 

n = 10
k = 2
print("Value fo P(", n, ", ", k, ") is ", permutationCoeff1(n, k), sep = "")


# A O(n) solution that uses table fact[] to calculate  the Permutation Coefficient 
  
# Returns value of Permutation Coefficient P(n, k)

def permutationCoeff2(n, k):
	fact = [0 for i in range (n+1)]
	# base case
	fact[0] = 1
	# calculate value factorials up to n 
	for i in range (1, n+1):
		fact[i] = i * fact[i-1]
	return int(fact[n]/fact[n-k])

print(permutationCoeff2(n,k))

def permutationCoeff3(n, k):
	Fn = 1
	# compute n! and (n-k)!
	for i in range(1, n+1):
		Fn *= i
		if (i == n-k):
			Fk = Fn
	coeff = Fn//Fk
	return coeff

print(permutationCoeff3(n,k))