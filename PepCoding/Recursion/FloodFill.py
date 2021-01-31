def mazepath(maze,row,col,pathSoFar,visited):
    if(row<0 or col<0 or row==len(maze) or col==len(maze[0]) or maze[row][col]==1 or visited[row][col]==True):
        return
    if row==len(maze)-1 and col==len(maze[0])-1:
        print(pathSoFar)
        return
    
    visited[row][col]=True
    mazepath(maze,row-1,col,pathSoFar+"t",visited)
    mazepath(maze,row,col-1,pathSoFar+"l",visited)
    mazepath(maze,row+1,col,pathSoFar+"d",visited)
    mazepath(maze,row,col+1,pathSoFar+"r",visited)
    visited[row][col]=False





n,m=map(int,input().split())
a=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    a.append(l)
visited=[[False for i in range(m)] for j in range(n)]
mazepath(a,0,0,"",visited)



