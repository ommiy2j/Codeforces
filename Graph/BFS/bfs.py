from queue import Queue
v=int(input())
edges=int(input())
graph=[[] for i in range(v)]
for i in range(edges):
    arr=[int(i) for i in input().split()]
    v1=arr[0]
    v2=arr[1]
    w=arr[2]
    graph[v1].append([v1,v2,w])
    graph[v2].append([v2,v1,w])
src=int(input())
visited=[False for i in range(v)]
q=Queue(maxsize=v)
q.put([src,str(src)+''])
while(q.qsize()>0):
    pair=q.get()
    if(visited[pair[0]]==True):
        continue
    visited[pair[0]]=True
    print(str(pair[0])+'@'+pair[1])
    for i in range(len(graph[pair[0]])):
        if(visited[graph[pair[0]][i][1]]==False):
            q.put([graph[pair[0]][i][1],pair[1]+str(graph[pair[0]][i][1])])