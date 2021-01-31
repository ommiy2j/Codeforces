
        

def Nqueen(chess,qsf,row):
    if row==len(chess):
        print(qsf + ".")
        return
    
    for col in range(len(chess)):
        if isQueenSafe(chess,row,col)==True:
            chess[row][col]=1
            Nqueen(chess,qsf+str(row)+"-"+str(col)+", ",row+1)
            chess[row][col]=0
        



def isQueenSafe(chess,row,col):
    i=row-1
    j=col-1
    while(i>=0 and j>=0):
        if chess[i][j]==1:
            return False
        i-=1
        j-=1

    i=row-1
    j=col
    while(i>=0):
        if chess[i][j]==1:
            return False
        i-=1
    r=row-1
    c=col+1
    while(r>=0 and c<len(chess)):
        if chess[r][c]==1:
            return False
        r-=1
        c+=1
        
    return True
n=int(input())
chess=[[0 for i in range(n)] for i in range(n)]
Nqueen(chess,"",0)