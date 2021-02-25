n=len(m)
y=len(m[0])
for i in range(n):
    for j in range(n-1,i,-1):
        m[i][j],m[j][i]=m[j][i],m[i][j]
return m