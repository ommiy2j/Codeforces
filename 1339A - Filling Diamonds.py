t=int(input())
for i in range(t):
    n=int(input())
    x=4*n-2
    if x==1:
        print(1)
    elif x%2==0:
        print(n)
    else:
        print(n+1)