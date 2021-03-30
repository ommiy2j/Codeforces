def displaygraph(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j],end=' ')
        print()
    print()
def knighttour(graph,r,c,move):
    if(r<0 or c<0 or r>=len(graph) or c>=len(graph) or graph[r][c]>0):
        return
    elif (move==len(graph)*len(graph)):
        graph[r][c]=move
        displaygraph(graph)
        graph[r][c]=0
        return
    graph[r][c]=move
    knighttour(graph,r-2,c+1,move+1)
    knighttour(graph,r-1,c+2,move+1)
    knighttour(graph,r+1,c+2,move+1)
    knighttour(graph,r+2,c+1,move+1)
    knighttour(graph,r+2,c-1,move+1)
    knighttour(graph,r+1,c-2,move+1)
    knighttour(graph,r-1,c-2,move+1)
    knighttour(graph,r-2,c-1,move+1)
    graph[r][c]=0


n=int(input())
r=int(input())
c=int(input())
graph=[[0 for i in range(n)]for i in range(n)]
knighttour(graph,r,c,1)