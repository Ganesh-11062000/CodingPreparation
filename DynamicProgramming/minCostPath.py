# https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/tutorial/


# minCost(x,y) = min(minCost(x-1,y),minCost(x,y-1)) + Cost[x][y]

dp = [[-1 for j in range(len(string2))] for i in range(len(string1))]
dp[0][0] = cost[0][0]

def minPath(cost,x,y,m,n):


	# base case for row
	for j in range(1,n):
		dp[0][j] = dp[0][j-1] + cost[0][j]

	#base case for col
	for i in range(1,m):
		dp[i][0] = dp[i-1][0] + cost[i][0]


	for i in range(1,x):
		for j in range(1,y):
			top = dp[i-1][j]
			left = dp[i][j-1]

			dp[i][j] = min(top,left) + cost[i][j]


	return dp[x-1][y-1]






# 0,0 -> x,y
# ans = minCost(x,y)