from collections import defaultdict

# directed graph
class Graph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def dfsUtil(self,u,visited,stack):
		visited[u] = True
		stack[u] = True

		isCyclePresent = False

		for v in self.graph[u]:
			if stack[v] == True:
				return True
			if visited[v] == False:
				isCyclePresent = isCyclePresent or self.dfsUtil(v,visited,stack)

		for v in self.graph[u]:
			stack[v] = False

		return isCyclePresent


	def dfs(self,start):
		visited = [False for i in range(self.V)]
		stack = [False for i in range(self.V)]

		cyclePresent = self.dfsUtil(start,visited,stack)
		return cyclePresent


def driver():
	# vertices = 4
	# Edges = [(0,1),(0,2),(1,2),(2,0),(2,3),(3,3)]

	vertices = 4
	Edges = [(0,1),(1,2),(3,0),(2,3)]

	g = Graph(vertices)

	for u,v in Edges:
		g.addEdge(u,v)

	print("Cycle is Present:",g.dfs(0))

driver()