n=int(input())
temp=[-1 for i in range(n)]
c=0
while n!=0:
    ns=list(str(n))
    m=max(ns)
    n=n-int(m)
    c+=1
print(c)
        
    