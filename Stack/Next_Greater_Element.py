# Given an array, print the Next Greater Element (NGE) for every element. 
# The Next greater Element for an element x is the first greater element on the right side of x in array. 
# Elements for which no greater element exist, consider next greater element as -1.

'''
def nextGreater(arr):
	res = [-1 for i in range(len(arr))]

	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[j] > arr[i]:
				res[i] = arr[j]
				break

	return res

# a = [4,5,2,25]
a = [13,7,6,12]
print(nextGreater(a))

Time Complexity = O(n^2)
'''

def nextGreater(arr):
	res = [-1 for i in range(len(arr))]
	stack = []

	stack.append(arr[-1])

	for i in range(len(arr)-2,-1,-1):
		if len(stack) == 0:
			stack.append(arr[i])
		else:
			if stack[-1] > arr[i]:
				res[i] = stack[-1]
				stack.append(arr[i])
			else:
				while len(stack) != 0 and stack[-1] <= arr[i]:
					stack.pop(-1)

				if len(stack) == 0:
					stack.append(arr[i])
				else:
					res[i] = stack[-1]
					stack.append(arr[i])

	return res



a = [13,7,6,12]
# a = [4,5,2,25]
print(nextGreater(a))