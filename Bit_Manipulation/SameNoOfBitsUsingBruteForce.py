def countSetbit(n):
    rsbm=n&-n
    c=0
    while n!=0:
        n-=rsbm
        rsbm=n&-n
        c+=1
    return c
n=int(input())
c=0
setBitIn_n=countSetbit(n)
for i in range(n):
    x=countSetbit(i)
    if x==setBitIn_n:
        c+=1
print(c)
