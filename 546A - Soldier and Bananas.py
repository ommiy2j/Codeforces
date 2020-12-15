k,n,w=map(int,input().split())
i=1
t=0
while(i<=w):
    t+=k*i
    i+=1
if(t-n<0):
    print(0)
else:
    print(t-n)
    
        