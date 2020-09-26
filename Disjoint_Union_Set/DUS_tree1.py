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
	W = [1,2,6,4,2,0,3]
	
	# Edges = dict()
	# Edges[(1,2)] = 1
	# Edges[(1,3)] = 1
	# Edges[(2,4)] = 1
	# Edges[(2,5)] = 1
	# Edges[(4,6)] = 1
	# Edges[(6,7)] = 1

	Edges = [(1, 2), (1, 3), (2, 4),(2, 5), (4, 6), (6, 7)]

	dus = DisjointUnionSet(7)

	for u,v in Edges:
		if W[u-1]%2==0 and W[v-1]%2==0:
			dus.union(u-1,v-1)

	dus.display()

	p = max(set(dus.parent),key=dus.parent.count)
	# print(p)

	print("Output =",dus.parent.count(p))

driver()



