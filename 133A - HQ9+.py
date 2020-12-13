s=list(input())
l=['H','Q','9']
c=0
for i in s:
    if i in l:
        c+=1
if(c>0):
    print("YES")
else:
    print("NO")