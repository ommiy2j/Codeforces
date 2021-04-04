n=int(input())
i=0
while(n>=0):
    x=(i*(i+1))//2
    if(n>=x):
        n=n-x
        i+=1
    else:
        i-=1
        break
    
print(i)