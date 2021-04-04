import itertools
for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    pos=[0 for i in range(n+1)]
    for i in range(n):
        pos[l[i]]=i
    end=n
    for i in range(n,-1,-1):
        start=pos[i]
        if(start<end):
            for j in range(start,end):
                print(l[j],end=' ')
            end=start
    print()


