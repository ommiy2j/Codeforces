for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ex=0
    c=1
    for i in range(n):
        if(a[i]>i):
            ex+=a[i]-i
            c=1
        elif(a[i]+ex>=i):
            ex-=(i-a[i])
            c=1
        else:
            c=0
            break
    if(c==1):
        print("YES")
    else:
        print("NO")