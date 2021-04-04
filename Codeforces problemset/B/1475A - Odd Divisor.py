for i in range(int(input())):
    n=int(input())
    if n%2!=0:
        print("YES")
    else:
        rsbm=n&-n
        c=0
        while(n):
            n=n-rsbm
            rsbm=n&-n
            c+=1
        if c==1:
            print("NO")
        else:
            print("YES")
