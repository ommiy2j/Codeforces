n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
t=[0 for i in range(n)]
t[0]=1
for i in range(1,n):
    m=0
    for j in range(i,-1,-1):
        if l[i]>=l[j]:
            m=max(t[j],m)
        t[i]=m+1
print(max(t))