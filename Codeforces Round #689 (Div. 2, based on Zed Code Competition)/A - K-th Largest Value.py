n,q=map(int,input().split())
a=[int(i) for i in input().split()]
one=0
for i in a:
    if i==1:
        one+=1
for i in range(q):
    t,x=map(int,input().split())
    if t==2:
        if x<=one:
            print(1)
        else:
            print(0)
    else:
        if a[x-1]==1:
            one-=1
            a[x-1]=0
        else:
            one+=1
            a[x-1]=1