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

		# if self.rank[parentX] < self.rank[parentY]:
		# 	self.parent[parentX] = parentY
		# elif self.rank[parentY] < self.rank[parentX]:
		# 	self.parent[parentY] = parentX
		# else:
		# 	self.rank[parentY] += 1
		# 	self.parent[parentX] = parentY

		if parentX <= parentY:
			self.parent[y] = parentX
		else:
			self.parent[x] = parentY


	def display(self):
		print("Rank   = {}".format(self.rank))
		print("Parent = {}".format(self.parent))


	def eightNeighbours(self,matrix,i,j,r,c):
		X = []
		Y = []
		if i-1>=0:
			if j-1>=0 and matrix[i-1][j-1] == 1:
				X.append(i-1)
				Y.append(j-1)
			if j+1<c and matrix[i-1][j+1] == 1:
				X.append(i-1)
				Y.append(j+1)
			if matrix[i-1][j] == 1:
				X.append(i-1)
				Y.append(j)

		if j-1>=0 and matrix[i][j-1] == 1:
				X.append(i)
				Y.append(j-1)
		if j+1<c and matrix[i][j+1] == 1:
			X.append(i)
			Y.append(j+1)

		if i+1<r:
			if j-1>=0 and matrix[i+1][j-1] == 1:
				X.append(i+1)
				Y.append(j-1)
			if j+1<c and matrix[i+1][j+1] == 1:
				X.append(i+1)
				Y.append(j+1)

			if matrix[i+1][j] == 1:
				X.append(i+1)
				Y.append(j)

		return X,Y


	def numberOfIslands(self,matrix,r,c):
		
		
		for i in range(r):
			for j in range(c):
				if matrix[i][j] == 1:
					X,Y = self.eightNeighbours(matrix,i,j,r,c)

					for k in range(len(X)):
						x = X[k]
						y = Y[k]

						if not self.isConnected(r*x+y,r*i+j):
							self.union(r*x+y,r*i+j)

						# print(r*x+y)
						# print(r*i+j)
						# print(self.parent)

		return self.parent


# 2*r + 4 => 9

def driver():

	matrix = [
		[1, 1, 0, 0, 0],
		[0, 1, 0, 0, 1],
		[1, 0, 0, 1, 1],
		[0, 0, 0, 0, 0],
		[1, 0, 1, 0, 1]
	]

	rows = 5
	cols = 5

	dsu = DisjointUnionSet(rows*cols)
	parent = dsu.numberOfIslands(matrix,rows,cols)

	islands = defaultdict(int)
	print(islands)

	for i in range(rows):
		for j in range(cols):
			if matrix[i][j] == 1:
				islands[parent[rows*i+j]] += 1


	print(islands)



driver()