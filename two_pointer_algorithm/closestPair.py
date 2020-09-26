# Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.

def closestPair(arr1,arr2,val):
	arr1.sort()
	arr2.sort()

	l,r = 0,len(arr2)-1
	diff = 99999

	while(l < len(arr1) and r >= 0):
		if abs(arr1[l]+arr2[r]-val) < diff:
			diff = abs(arr1[l]+arr2[r]-val)
			u = arr1[l]
			v = arr2[r]

		if arr1[l]+arr2[r] > val:
			r -= 1

		elif arr1[l] + arr2[r] < val:
			l += 1

		else:
			break

	return u,v


# a1 = [1,4,5,7]
# a2 = [10,20,30,40]
# v = 32

a1 = [1,4,5,7]
a2 = [10,20,30,40]
v = 50
print(closestPair(a1,a2,v))
	