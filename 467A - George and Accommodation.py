n=int(input())
c=0
for i in range(n):
    p,q=input().split()
    p=int(p)
    q=int(q)
    if(p==q):
        pass
    else:
        if(abs(p-q)>=2):
            c+=1
print(c)
            