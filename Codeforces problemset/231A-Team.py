n=int(input())
newlst=[]
for i in range(n):
    c=0
    lst=list(map(int,input().split()))
    for i in lst:
        if i==1:
            c+=1
        else:
            pass
    newlst.append(c)
a=0
for i in newlst:
    if(i>=2):
        a+=1
print(a)
    