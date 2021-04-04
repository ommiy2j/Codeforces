from queue import Queue


def transitiveClousure(graph,src,visited,osrc):
    for i in range(len(graph[src])):
        if visited[osrc][graph[src][i][1]]==0:
            visited[osrc][graph[src][i][1]]=1
            transitiveClousure(graph,graph[src][i][1],visited,osrc)


v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    v1,v2=map(int,input().split())
    graph[v1].append([v1,v2])
visited=[[0 for i in range(v)] for i in range(v)]
for i in range(v):
    transitiveClousure(graph,i,visited,i)
print(visited)
        
