n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
t=[0 for i in range(n)]
t[0]=1
for i in range(1,n):
    for j in range(i,-1,-1):
        if(a[j]>a[i]):
            t[i]=i-j
            break
    if t[i]==0:
        t[i]=i+1
for i in t:
    print(i)
        

