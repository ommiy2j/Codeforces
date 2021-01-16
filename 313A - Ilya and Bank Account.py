n=int(input())
if n>0:
    print(n)
else:
    n=-(n)
    if len(str(n))>2:
        a=n//10
        b=int(str(a//10)+str(n%10))
        if a>b:
            print(-b)
        else:
            print(-a)
    elif len(str(n))==2:
        a=n//10
        b=n%10
        print(a,b)
        if a>b:
            print(-b)
        else:
            print(-a)