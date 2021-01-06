def powerOf2(n):
    rsbm=n & (-n)
    c=0
    while (n!=0):
        n=n-rsbm
        rsbm=n & -n
        c+=1
    return c     
n=int(input())
x=powerOf2(n)
if x==1:
    print(1)
else:
    print(x)
    
