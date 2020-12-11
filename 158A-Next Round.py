n,k=input().split()
n,k=int(n),int(k)
lst=list(map(int,input().split()))
a=lst[k-1]
c=0
for i in lst:
    if(i>=a and i!=0):
        c+=1
print(c)