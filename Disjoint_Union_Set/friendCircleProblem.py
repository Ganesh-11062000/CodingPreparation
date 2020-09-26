class DisjointUnionSet:
    def __init__(self,vertices):
        self.V = vertices
        self.parent = [i for i in range(vertices)]
        
    def find(self,x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def isConnected(self,x,y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False
        
    def union(self,x,y):
        if self.isConnected(x,y):
            return
        
        parentX = self.find(x)
        parentY = self.find(y)
        
        if parentX < parentY:
            # self.parent[y] = parentX
            for i in range(self.V):
                if self.parent[i] == parentY:
                    self.parent[i] = parentX 
        else:
            # self.parent[x] = parentY
            for i in range(self.V):
                if self.parent[i] == parentX:
                    self.parent[i] = parentY
            
    
class Solution:
    def findCircleNum(self, M):
        
        rows = len(M[0])
        cols = len(M[0])
        
        dus = DisjointUnionSet(rows)
        
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    if not dus.isConnected(i,j):
                        dus.union(i,j)
                        print(dus.parent)

                


                   
        # print(dus.parent)     
        print(list(set(dus.parent)))         
        return len(list(set(dus.parent)))
        

             
# M = [
#     [1,1,0],
#     [1,1,0],
#     [0,0,1]
# ]   

M = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]

# (0,0),(0,3),(1,1),(1,2),(2,1),(2,2),(2,3)
# (3,0),(3,2),(3,3)

# 0 1 0 0
# 0 1 2 3


s = Solution()
s.findCircleNum(M)    
        
        
        
# (0,0)(0,1)(1,0),(1,1),(2,2)
# (0,0)(0,1)(1,0),(1,1),(1,2),(2,1),(2,2)
        