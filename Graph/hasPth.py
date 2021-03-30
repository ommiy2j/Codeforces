def hasPath(graph,src,dest,visited):
    if src==dest:
        return True
    visited[src]=True
    for i in range(len(graph[src])):
        if(visited[graph[src][i][1]]==False):
            neighbour_HasPath=hasPath(graph,graph[src][i][1],dest,visited)
            if(neighbour_HasPath==True):
                return True
    return False



v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    arr=list(map(int,input().split()))
    v1=arr[0]
    v2=arr[1]
    w=arr[2]
    graph[v1].append([v1,v2,w])
    graph[v2].append([v2,v1,w])
src=int(input())
dest=int(input())
visited=[False for i in range(v)]
ans=hasPath(graph,src,dest,visited)
print(ans)
    
