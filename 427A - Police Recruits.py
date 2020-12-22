n=int(input())
l=[int(i) for i in input().split()]
sum=0
c=0
for i in range(n):
    if(l[i]>0):
        sum+=l[i]
    elif(sum>0):
        sum-=1
    else:
        c+=1
print(c)  