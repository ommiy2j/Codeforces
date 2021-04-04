for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    l.sort()
    max=999999
    for i in range(n-1):
        if abs(l[i]-l[i+1])<max:
            max=abs(l[i]-l[i+1])
    print(max)
        