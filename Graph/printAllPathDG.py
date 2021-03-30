def printAllPath(graph,src,dest,visited,psf):
    if src==dest:
        print(psf)
        return
    visited[src]=True
    for i in range(len(graph[src])):
        if(visited[graph[src][i][1]]==False):
            printAllPath(graph,graph[src][i][1],dest,visited,psf+str(graph[src][i][1]))
    visited[src]=False
    



v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    arr=[int(i) for i in input().split()]
    v1=arr[0]
    v2=arr[1]
    w=arr[2]
    graph[v1].append([v1,v2,w])
    # graph[v2].append([v2,v1,w])
src=int(input())
dest=int(input())
visited=[False for i in range(v)]
printAllPath(graph,src,dest,visited,str(src)+'')
# print(graph)
    