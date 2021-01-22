def check(n):
    c=0
    rsbm=n&-n
    while(n):
        n=n-rsbm
        rsbm=n&-n
        c+=1
    return c
a=int(input())
b=int(input())
n=a^b
print(check(n))