n,v=map(int,input().split())
if v>=n:
    print(v)
else:
    p=v
    for i in range(2,n-v+1):
        p+=i
    print(p)
    
        
    