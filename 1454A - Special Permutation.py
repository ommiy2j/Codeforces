t=int(input())
for i in range(t):
    n=int(input())
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    for i in range(1,len(lst)):
        if(lst.index(lst[i])+1==lst[i]):
            lst[i-1],lst[i]=lst[i],lst[i-1]
    for i in range(len(lst)):
        print(lst[i],end=' ')
    print()