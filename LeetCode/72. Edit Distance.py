def minDist(w1,w2):
    t=[[0 for i in range(len(w1)+1)] for i in range(len(w2)+1)]
    for i in range(len(w2)+1):
        t[i][0]=i
    for i in range(len(w1)+1):
        t[0][i]=i

    for i in range(1,len(w2)+1):
        for j in range(1,len(w1)+1):
            if w2[i-1]==w1[j-1]:
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]=min(t[i-1][j],t[i][j-1],t[i-1][j-1])+1
                
    return t[-1][-1]


w1='intention'
w2='execution'
print(minDist(w1,w2))
