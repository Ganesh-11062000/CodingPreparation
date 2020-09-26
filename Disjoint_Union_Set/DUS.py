# implementation using rank and path compression
# optimized code

class DisjointUnionSet:
	def __init__(self,n):		#n = no. of nodes
		self.rank = [1]*n
		self.parent = [i for i in range(n)]


	def find(self,x):
		if self.parent[x] == x:
			return x
		else:
			self.parent[x] = self.find(self.parent[x])	#path compression
			return self.parent[x]

	def isConnected(self,x,y):
		if self.parent[x] == self.parent[y]:
			return True
		else:
			return False


	def union(self,x,y):
		if self.parent[x] == self.parent[y]:
			return

		parentX = self.parent[x]
		parentY = self.parent[y]

		if self.rank[parentX] < self.rank[parentY]:
			self.parent[parentX] = parentY
		elif self.rank[parentY] < self.rank[parentX]:
			self.parent[parentY] = parentX
		else:
			self.rank[parentY] += 1
			self.parent[parentX] = parentY


	def display(self):
		print("Rank   = {}".format(self.rank))
		print("Parent = {}".format(self.parent))


def driver():
	dus = DisjointUnionSet(5)

	dus.union(0,2)
	dus.display()

	dus.union(4,2)
	dus.display()

	dus.union(3,1)
	dus.display()

	print("{} {} is connected : {}".format(0,4,dus.isConnected(0,4)))
	print("{} {} is connected : {}".format(0,1,dus.isConnected(0,1)))
	print("{} {} is connected : {}".format(3,4,dus.isConnected(3,4)))


driver()