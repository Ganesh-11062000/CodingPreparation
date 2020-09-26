class DisjointUnionSet:
    def __init__(self,n):        #n = no. of nodes
        self.rank = [1]*n
        self.parent = [i for i in range(n)]


    def find(self,x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])    #path compression
            return self.parent[x]

    def isConnected(self,x,y):
        if self.parent[x] == self.parent[y]:
            return True
        else:
            return False


    def union(self,x,y):
        

        # parentX = self.parent[x]
        # parentY = self.parent[y]

        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return

        if self.rank[parentX] < self.rank[parentY]:
            self.parent[parentX] = parentY
        elif self.rank[parentY] < self.rank[parentX]:
            self.parent[parentY] = parentX
        else:
            self.rank[parentY] += 1
            self.parent[parentX] = parentY

        # if parentX <= parentY:
        #     # self.parent[parentY] = parentX
        #     for i in range(len(self.parent)):
        #     	if self.parent[i] == parentY:
        #     		self.parent[i] = parentX
        # else:
        #     # self.parent[parentX] = parentY
        #     for i in range(len(self.parent)):
        #     	if self.parent[i] == parentX:
        #     		self.parent[i] = parentY


    # def display(self):
    #     print("Rank   = {}".format(self.rank))
    #     print("Parent = {}".format(self.parent))

def componentsInGraph(gb):
    #
    # Write your code here.
    #
    nodes = set()
    for g,b in gb:
    	nodes.add(g)
    	nodes.add(b)

    n = len(list(nodes))
    # print(n)

    dus = DisjointUnionSet(2*(len(gb)))
    for g,b in gb:
        if not dus.isConnected(g-1,b-1):
            dus.union(g-1,b-1)
            print(dus.parent)

    for i in range(2*len(gb)):
    	dus.find(i)

    print(dus.parent)
			 		

    p = []
    for i in range(2*(len(gb))):
    	if i+1 in nodes:
    		p.append(dus.parent[i])

    print(p) 

    p1 = max(set(p),key=p.count)
    p2 = min(set(p),key=p.count)

    c1 = p.count(p1)
    c2 = p.count(p2)

    l = [c2,c1]
    print(l)
    # return l


gb = [[1,6],[2,7],[3,8],[4,9],[2,6]]
componentsInGraph(gb)
