for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    temp=[-1 for i in range(n)]
    for i in range(n-1,-1,-1):
        if i+l[i]+1>n:
            temp[i]=l[i]
        else:
            a=l[i]+temp[i+l[i]]
            temp[i]=a
    print(max(temp))
                

    