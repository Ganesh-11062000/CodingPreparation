from collections import defaultdict

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

	# Edges = [(0,1),(1,2),(2,0)]
	# vertices = 3

	Edges = [(0,1),(0,2),(0,3),(1,2),(3,4)]
	vertices = 5

	dus = DisjointUnionSet(vertices)
	cyclePresent = False

	for u,v in Edges:
		if dus.isConnected(u,v):
			cyclePresent = True
			print("{} {}".format(u,v))
			break
		else:
			dus.union(u,v)

	print("Cycle is Present:",cyclePresent) 


driver()