import math
for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    c=0
    for i in range(1,n):
        maxv=max(l[i],l[i-1])
        minv=min(l[i],l[i-1])
        while((maxv/minv)>2):
            maxv=maxv/2
            c+=1
    print(c)