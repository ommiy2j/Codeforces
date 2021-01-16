for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    odd=0
    even=0
    f=0
    for i in range(n):
        if i%2==a[i]%2:
            f+=1
        elif i%2==0:
            if a[i]%2!=0:
                even+=1
        else:
            odd+=1
    if even==odd:
        print(even)
    else:
        print(-1)
        

        