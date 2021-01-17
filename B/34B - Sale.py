n,m=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()
c=0
for i in range(m):
    if a[i]>0:
        pass
    else:
        c+=a[i]
print(abs(c))