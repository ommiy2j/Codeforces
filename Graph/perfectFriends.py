def getconnected(graph,src,visited,connecv):
    connecv.append(src)
    visited[src]=True
    for i in range(len(graph[src])):
        if visited[graph[src][i][1]]==False:
            getconnected(graph,graph[src][i][1],visited,connecv)
    
    
    

v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    v1,v2=map(int,input().split())
    graph[v1].append([v1,v2])
    graph[v2].append([v2,v1])


visited=[False for i in range(v)]
comps=[]
for i in range(v):
    if visited[i]==False:
        connecv=[]
        getconnected(graph,i,visited,connecv)
        comps.append(connecv)
        
total=0
for i in range(len(comps)-1):
    for j in range(i+1,len(comps)):
        total+=len(comps[i])*len(comps[j])
print(total)