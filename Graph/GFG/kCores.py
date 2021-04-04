class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[[] for i in range(v)]
    def addEdge(self,v1,v2):
        if v1==v2:
            self.graph[v1].append([v1,v2])
        else:
            self.graph[v1].append([v1,v2])
            self.graph[v2].append([v2,v1])
    def print_graph(self):
        return self.graph
    

    def printKCores(self,k):
        deg=[0 for i in range(self.v)]
        for i in range(self.v):
            deg[i]=len(self.graph[i])
        visited=[False for i in range(self.v)]
        for i in range(self.v):
            if visited[i]==False:
                self.dfs(i,visited,deg,k)
        return deg
            
    def dfs(self,src,visited,deg,k):
        visited[src]=True
        for i in range(len(self.graph[src])):
            if deg[src]<k:
                deg[self.graph[src][i][1]]-=1
            if visited[self.graph[src][i][1]]==False:
                self.dfs(self.graph[src][i][1],visited,deg,k)
        
        
        
        
g1 = Graph (9);
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
print(g1.printKCores(3))
