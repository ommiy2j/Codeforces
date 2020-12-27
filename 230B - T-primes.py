import math

def prime(n):
    if n<2:
        return False
    else:
        x=2
        while(x<=math.sqrt(n)):
            if(n%x==0):
                return False
            x+=1
        return True


n=int(input())
l=[int(i) for i in input().split()]
for i in l:
    x=math.sqrt(i)
    x=int(x)
    if(x*x==i and prime(x)):
        print("YES")
    else:
        print("NO")
    
    