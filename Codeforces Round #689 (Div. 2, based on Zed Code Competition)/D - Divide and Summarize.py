t=int(input())
for i in range(t):
    n,q=input().split()
    n,q=int(n),int(q)
    lst=[int(i) for i in input().split()]
    clst=[]
    for j in range(q):
        clst.append(input())
        clst=[int(i) for i in clst]
    lst.sort()
    s=[]
    s.append(sum(lst))
    mid=lst[0]+lst[len(lst)-1]//2
    l=lst[0:mid]
    right=[]
    for i in lst:
        if i in l:
            pass
        else:
            right.append(i)
    while(len(lst)!=1):
        if(min(lst)==max(lst)):
            break
        else:
            mid=min(lst)+max(lst)//2
            if(mid==len(lst)):
                left=lst[0:mid-1]
            else:
                left=lst[0:mid]
            s.append(sum(left))
            lst=left
    s.append(sum(right))
    
    for x in clst:
        if x in s:
            print("YES")
        else:
            print("NO")
    