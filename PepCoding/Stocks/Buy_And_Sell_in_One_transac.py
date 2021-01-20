n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
t=[0 for i in range(n)]
t[0]=l[0]
for i in range(1,n):
    m=0
    for j in range(i,-1,-1):
        x=l[i]-l[j]
        m=max(m,x)
    t[i]=m
print(max(t[1:]))