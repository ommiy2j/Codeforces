def getConnected(graph,src,allconnected,visited):
    allconnected.append(src)
    visited[src]=True
    for i in range(len(graph[src]))    :
        if(visited[graph[src][i][1]]==False):
            getConnected(graph,graph[src][i][1],allconnected,visited)



v=int(input())
edge=int(input())
graph=[[] for i in range(v)]
for i in range(edge):
    arr=[int(i) for i in input().split()]
    v1=arr[0]
    v2=arr[1]
    w=arr[2]
    graph[v1].append([v1,v2,w])
    graph[v2].append([v2,v1,w])
allconnected=[]
visited=[False for i in range(v)]
for i in range(v):
    if(visited[i]==False):
        connv=[]
        getConnected(graph,i,connv,visited)
        allconnected.append(connv)
print(allconnected)