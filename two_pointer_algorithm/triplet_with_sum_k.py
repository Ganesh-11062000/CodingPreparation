# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. If there is such a triplet present in array, then print the triplet and return true. Else return false.

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

def tripletPresent(arr,val):
	arr.sort()
	triplets = []

	for i in range(len(arr)-2):
		present,v,w = isPresent(arr[i+1:],val-arr[i])
		if present == True:
			triplets.append((arr[i],v,w))

	return triplets


# a = [12,3,4,1,6,9]
# k = 24

a = [1,2,3,4,5]
k = 9
print(tripletPresent(a,k))



