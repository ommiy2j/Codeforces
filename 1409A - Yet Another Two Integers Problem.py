for i in range(int(input())):
    a,b=map(int,input().split())
    x=abs(a-b)
    c=x%10
    y=x//10
    if(c==0):
        print(x//10)
    else:
        print(y+1)
            