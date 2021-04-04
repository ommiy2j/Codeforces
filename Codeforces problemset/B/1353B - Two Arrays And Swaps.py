for i in range(int(input())):
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort(reverse=True)
    m=sum(a)
    for i in range(k):
        a[i]=b[i]
        if sum(a)>m:
            m=sum(a)
    print(m)
        
        