import math
for i in range(int(input())):
    n=int(input())
    t=[]
    c=0
    a=[int(i) for i in input().split()]
    for i in range(n):
        m=int(math.log(a[i])/math.log(2))+1
        if m in t:
            c+=1
        else:
            t.append(m)
    print(c)
        