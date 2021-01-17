for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        d=a-b
        if d%2==0:
            c=1
        else:
            c=2
    elif a==b:
        c=0
    else:
        d=a-b
        if d%2!=0:
            c=1
        else:
            c=2
    print(c)