for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    l.sort()
    c=0
    if(len(l)==1):
        print("YES")
        break
    for i in range(n-1):
        if abs(l[i]-l[i+1])<=1:
            c+=1
        else:
            c=0
            break
    if c==0:
        print("NO")
    else:
        print("YES")
            
            