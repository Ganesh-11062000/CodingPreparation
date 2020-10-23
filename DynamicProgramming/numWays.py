# https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/tutorial/

'''
numWays(x,y) = numWays(x-1,y) + numWays(x,y-1)

def numWays(x,y,m,n):


	# base case for row
	for j in range(1,n):
		dp[0][j] = 1

	#base case for col
	for i in range(1,m):
		dp[i][0] = 1

	for i in range(x):
		for j in range(y):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]


	return dp[x-1][y-1]


dp = [[-1 for j in range(len(string2))] for i in range(len(string1))]
dp[0][0] = 1
'''

Level - 2 (blocked cells) 
M[i][j] = X implies blocked

numWays(x,y) = numWays(x-1,y) + numWays(x,y-1)

def numWays(x,y,m,n):

	if M[0][0] == "X":
		return 0

	# base case for row
	for j in range(1,n):
		if M[0][j] == "X":
			dp[0][j] = 0
		else:
			dp[0][j] = dp[0][j-1]

	#base case for col
	for i in range(1,m):
		if M[i][0] == "X":
			dp[i][0] = 0
		else:
			dp[i][0] = dp[i-1][0]

	for i in range(x):
		for j in range(y):
			dp[i][j] = 0

			if M[i-1][j] != "X":
				dp[i][j] += dp[i-1][j]

			if M[i][j-1] != "X":
				dp[i][j] += dp[i][j-1]


	return dp[x-1][y-1]


dp = [[-1 for j in range(len(string2))] for i in range(len(string1))]
dp[0][0] = 1