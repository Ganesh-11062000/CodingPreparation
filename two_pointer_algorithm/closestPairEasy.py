# Given a sorted array and a number x, find a pair in array whose sum is closest to x.

# array is already sorted
def closestPair(arr,val):
	i,j = 0,len(arr)-1

	diff = 999999
	while(i < j):
		if abs(arr[i]+arr[j]-val) < diff:
			diff = abs(arr[i]+arr[j]-val)
			u = arr[i]
			v = arr[j]

		if arr[i]+arr[j] > val:
			j -= 1
		elif arr[i]+arr[j] < val:
			i += 1
		else:
			break

	return u,v


# a = [10,22,28,29,30,40]
# v = 54

a = [1,3,4,7,10]
v = 15

print(closestPair(a,v))