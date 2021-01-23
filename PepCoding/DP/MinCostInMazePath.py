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

    
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if i==n-1 and j==m-1:
            dp[i][j]=arr[i][j]
        elif i==n-1:
            dp[i][j]=dp[i][j+1]+arr[i][j]
        elif j==m-1:
            dp[i][j]=dp[i+1][j]+arr[i][j]
        else:
            dp[i][j]=min(dp[i+1][j],dp[i][j+1])+arr[i][j]
print(dp[0][0])
