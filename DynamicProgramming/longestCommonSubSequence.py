'''
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/
string1 = "ABCDGH"
string2 = "AEDFHR"

logic - 
keep two pointers 
one is pointing to start of string 1 and other 
pointer points to start of string2

let pointers are pointing to ch1 and ch2 respectively.

if ch1 == ch2
then ptr1++ and ptr2++
else:
	try ptr1++ 
	try ptr2++

construct Recursive solution

'''

# Recursive code - O(2^n)
'''
def lcs(s1,s2,ptr1,ptr2):
	if ptr1 == len(s1) or ptr2 == len(s2):
		return 0

	if s1[ptr1] == s2[ptr2]:
		return 1 + lcs(s1,s2,ptr1+1,ptr2+1)
	

	left = lcs(s1,s2,ptr1+1,ptr2)
	right = lcs(s1,s2,ptr1,ptr2+1)

	return max(left,right)


string1 = "ABCDGH"
string2 = "AEDFHR"
#ADH

string1 = "AGGTAB"
string2 = "GXTXAYB"
# GTAB

print(lcs(string1,string2,0,0))
'''

# dp implementation - O(n^2)
# in recursive solution ptr1 and ptr2 are changing 


def lcs(s1,s2,ptr1,ptr2,dp):
	if ptr1 == len(s1) or ptr2 == len(s2):
		return 0

	if dp[ptr1][ptr2] != -1:
		return dp[ptr1][ptr2]

	if s1[ptr1] == s2[ptr2]:
		dp[ptr1][ptr2] = 1 + lcs(s1,s2,ptr1+1,ptr2+1,dp)
		return dp[ptr1][ptr2]

	left = lcs(s1,s2,ptr1+1,ptr2,dp)
	right = lcs(s1,s2,ptr1,ptr2+1,dp)

	dp[ptr1][ptr2] = max(left,right)

	return dp[ptr1][ptr2]



# string1 = "ABCDGH"
# string2 = "AEDFHR"
#ADH

string1 = "AGGTAB"
string2 = "GXTXAYB"
# GTAB

dp = [[-1 for j in range(len(string2))] for i in range(len(string1))]

print(lcs(string1,string2,0,0,dp))

s = ""

i = len(string1)-1
j = len(string2)-1

while i>=0 and j>=0:
	if string1[i] == string2[j]:
		s = string1[i] + s 
		i -= 1
		j -= 1

	if dp[i-1][j] > dp[i][j-1]:
		i -= 1
	else:
		j -= 1

print(s)



		


