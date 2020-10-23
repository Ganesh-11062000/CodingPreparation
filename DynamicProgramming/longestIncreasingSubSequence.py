# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

# arr = [50,3,10,7,40,80]
# 	    1 1  2 2 3  4 


def lis(arr,n):
	L = [1 for i in range(len(arr))]

	for i in range(1,len(arr)):
		x = 1
		for j in range(i):
			if arr[i]>arr[j]:
				if L[j] > x:
					x = L[j]+1
					



			print(L)

arr = [50,3,10,7,40,80]
lis(arr,len(arr))





