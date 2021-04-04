for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    diff=abs(a-b)
    x=a//b
    x=x*b
    a=a-x
    y=b-a
    if(y==b):
        print(0)
    else:
        print(y)
        
        