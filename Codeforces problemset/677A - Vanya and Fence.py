n,m=[int(i) for i in input().split()]
h=[int(i) for i in input().split()]
c=0
for i in h:
    if(i<=m):
        c+=1
    else:
        c+=2
print(c)