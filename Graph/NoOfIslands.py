def islands(graph,i,j,visited):
    if(i<0 or j<0 or i>=len(graph) or j>=len(graph[0]) or visited[i][j]==True):
        return
    if(graph[i][j]==1):
        return
    graph[i][j]=True
    islands(graph,i-1,j,visited)
    islands(graph,i,j+1,visited)
    islands(graph,i,j-1,visited)
    islands(graph,i+1,j,visited)

v=int(input())
edges=int(input())
graph=[]
for i in range(edges):
    a=[int(i) for i in input().split()]
    graph.append(a)

visited=[[False for i in range(len(graph))] for j in range(len(graph[0]))]
count=0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]==False and graph[i][j]==0:
            islands(graph,i,j,visited)
            count+=1
print(count)



# 1. You are given a 2d array where 0's represent land and 1's represent water. 
#      Assume every cell is linked to it's north, east, west and south cell.
# 2. You are required to find and count the number of islands.

#input
# 8
# 8
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1
# 1 1 1 1 1 1 1 0
# 1 1 0 0 0 1 1 0
# 1 1 1 1 0 1 1 0
# 1 1 1 1 0 1 1 0
# 1 1 1 1 1 1 1 0
# 1 1 1 1 1 1 1 0

#op
#3