for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    s=sum(l)
    l1=len(set(l))
    if l1==1 and n%2!=0:
        print("No")
    elif l1==1 and n%2==0:
        print('Yes')
    else:
        if s%2==0:
            print('Yes')
        else:
            print('No')