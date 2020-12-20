a=input()
b=input()
x=list(a+b)
x.sort()
d=list(input())
d.sort()
c=0
if(len(x)!=len(d)):
    print("NO")
else:
    for i in range(len(x)):
        if x[i] in d and x.count(x[i])==d.count(d[i]):
            pass
        else:
            c+=1
    if(c>0):
        print("NO")
    else:
        print("YES")
        
        