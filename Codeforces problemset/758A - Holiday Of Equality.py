n=int(input())
c=0
a=[int(i) for i in input().split()]
a.sort()
if n==1:
    print(0)
else:
    m=max(a)
    for i in range(n-1):
        c+=m-a[i]
    print(c)
            
