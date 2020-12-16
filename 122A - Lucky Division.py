n=int(input())
lst=[]
for i in range(1000):
    s=str(i)
    c=0
    for j in s:
        if(j=='4' or j=='7'):
            c+=1
    if(c==len(s)):
        lst.append(int(i))
f=False
for i in range(len(lst)):
    if(n%lst[i]==0):
        f=True
if(f==True):
    print("YES")
else:
    print("NO")

