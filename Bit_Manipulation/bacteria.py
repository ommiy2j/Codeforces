def powerOf2(n):
    rsbm=n & (-n)
    c=0
    while (n!=0):
        n=n-rsbm
        rsbm=n & -n
        c+=1
    if c==1:
        return True
    else:
        return False
    
        
n=int(input())
x=powerOf2(n)
if x:
    print(1)
else:
    print(2)
    
