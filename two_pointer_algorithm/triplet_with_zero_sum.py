# Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

def isPresent(arr,val):
	i,j = 0,len(arr)-1
	while(i < j):
		if arr[i]+arr[j] > val:
			j -= 1
		elif arr[i]+arr[j] < val:
			i += 1
		else:
			return True,arr[i],arr[j]

	return False,-1,-1

def tripletPresent(arr):
	arr.sort()
	triplets = []

	for i in range(len(arr)-2):
		present,v,w = isPresent(arr[i+1:],-arr[i])
		if present == True:
			triplets.append((arr[i],v,w))

	return triplets

# a = [0,-1,2,-3,1]
a = [1,-2,1,0,5]
print(tripletPresent(a))



