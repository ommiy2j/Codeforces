n=int(input())
m=int(input())
arr=[]
for i in range(n):
    x=[int(i) for i in input().split()]
    arr.append(x)

dp=[]
for i in range(n):
    x=[0 for i in range(m)]
    dp.append(x)

for j in range(m-1,-1,-1):
    for i in range(n-1,-1,-1):
        if j==m-1:
            dp[i][j]=arr[i][j]
        elif i==0:
            dp[i][j]=max(dp[i][j+1],dp[i+1][j+1])+arr[i][j]
        elif i==n-1:
            dp[i][j]=max(dp[i-1][j+1],dp[i-1][j+1])+arr[i][j]
        else:
            dp[i][j]=max(dp[i][j+1],dp[i+1][j+1],dp[i-1][j+1])+arr[i][j]
m=0
for i in range(n):
    m=max(m,dp[i][0])
print(m)
    
