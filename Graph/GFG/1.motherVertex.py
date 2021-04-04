from queue import Queue

def mothervertex(graph,src,visited):
    q=Queue(maxsize=v)
    q.put(src)
    while(q.qsize()>0):
        rem=q.get()
        if rem in visited:
            continue
        visited.add(rem)
        for i in range(len(graph[rem])):
            if graph[rem][i][1] not in visited:
                q.put(graph[rem][i][1])
    

v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    v1,v2=map(int,input().split())
    graph[v1].append([v1,v2])
for i in range(v):
    visited=set()
    x=mothervertex(graph,i,visited)
    if len(visited)==v:
        print(i)
        
