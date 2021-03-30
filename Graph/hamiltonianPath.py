def allpath(graph,src,visited,psf,osrc):
    if len(visited)==len(graph)-1:
        iscycle=False
        for i in range(len(graph[src])):
            if graph[src][i][1]==osrc:
                iscycle=True
        if iscycle:
            print(psf+'*')
        else:
            print(psf+'.')
        return
    visited.add(src)
    for i in range(len(graph[src])):
        if graph[src][i][1] not in visited:
            allpath(graph,graph[src][i][1],visited,psf+str(graph[src][i][1]),osrc)
    visited.remove(src)
    
    
    

v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    v1,v2,w=map(int,input().split())
    graph[v1].append([v1,v2,w])
    graph[v2].append([v2,v1,w])


visited=set()
src=int(input())
allpath(graph,src,visited,str(src)+'',osrc=src)