from queue import Queue

def isCyclic(graph,src,visited):
    q=Queue(maxsize=v)
    q.put(src)
    while(q.qsize()>0):
        rem=q.get()
        if visited[rem]==True:
            return True
        visited[rem]=True
        for i in range(len(graph[rem])):
            if visited[graph[rem][i][1]]==False:
                q.put(graph[rem][i][1])
    return False
    
    
    
v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    v1,v2,w=map(int,input().split())
    graph[v1].append([v1,v2,w])
    graph[v2].append([v2,v1,w])
visited=[False for i in range(v)]
x=0
for i in range(v):
    if(visited[i]==False):
        x=isCyclic(graph,i,visited)
        if x==True:
            x=1
if x==1:
    print('true')
else:
    print('false')
    
        
