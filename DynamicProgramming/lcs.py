# def lcs(i,j,s1,s2):

# 	if i == len(s1) or j == len(s2):
# 		return 0

# 	if dp[i][j] != -1:
# 		return dp[i][j]

# 	if s1[i] == s2[j]:		
# 		return 1 + lcs(i+1,j+1,s1,s2)
# 	else:
# 		left = lcs(i+1,j,s1,s2)
# 		right = lcs(i,j+1,s1,s2)

# 		dp[i][j] = max(left,right)
# 		return dp[i][j]


def lcs(s1,s2):
	dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			if s1[i] == s2[j]:
				dp[i][j] = dp[i-1][j-1]+1
			else:
				left = dp[i-1][j]
				right = dp[i][j-1]
				dp[i][j] = max(left,right)

	return dp[len(s1)-1][len(s2)-1]


s1 = "abd"
s2 = "abcd"
dp = [[-1 for i in range(len(s2))] for j in range(len(s1))]
print(lcs(s1,s2))



