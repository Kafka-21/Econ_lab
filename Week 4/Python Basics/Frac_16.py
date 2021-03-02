# Eggs dropping puzzle 

# function to reutnr the minimum number of trials needed in the worst case with n eggs and k floors
def eggDrop(n, k):
	dp = [[0 for i in range(n+1)]
			 for j in range(k+1)]
	x = 0
	# fill all the entries in table using optimal substructue property
	while (dp[x][n] < k):
		x += 1
		for i in range(1, n+1):
			dp[x][i] = dp[x-1][i-1] + dp[x-1][i] + 1
			print(dp[x][i])
	return x

n = 2
k = 10
print(eggDrop(n, k))
