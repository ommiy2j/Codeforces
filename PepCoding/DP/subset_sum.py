n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
sum=int(input())
a.sort()
t=[[0 for i in range(sum+1)] for i in range(len(a))]
for i in range(len(a)):
    t[i][0]=1
for i in range(len(a)):
    for j in range(sum+1):
        if j<a[i]:
            t[i][j]=t[i-1][j]
        if j>=a[i]:
            t[i][j]=t[i-1][j] or t[i-1][j-a[i]]
         
if t[-1][-1]==1:
    print("true")
else:
    print("false")