nums = [2,0,2,1,1,0]

c0,c1,c2 = nums.count(0),nums.count(1),nums.count(2)
print("{} {} {}".format(c0,c1,c2))

i = 0
while c0 :
	nums[i] = 0
	i += 1
	c0 -= 1

while c1 :
	nums[i] = 1
	i += 1
	c1 -= 1

while c2 :
	nums[i] = 2
	i += 1
	c2 -= 1

print(nums)