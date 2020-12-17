n=int(input())
lst=[int(i) for i in input().split()]
for i in range(1,n+1):
    for j in range(n):
        if(lst[j]==i):
            print(j+1,end=' ')
            break
    