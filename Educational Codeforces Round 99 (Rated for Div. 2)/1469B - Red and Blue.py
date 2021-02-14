for i in range(int(input())):
    n=int(input())
    r=[int(i) for i in input().split()]
    m=int(input())
    b=[int(i) for i in input().split()]
    m1=0
    s=0
    for i in range(n):
        s+=r[i]
        m1=max(m1,s)
    s2=0
    m2=0
    for i in range(m):
        s2+=b[i]
        m2=max(m2,s2)
    print(m1+m2)