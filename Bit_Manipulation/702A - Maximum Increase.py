n=int(input())
l=[int(i) for i in input().split()]
max=1
c=1
for i in range(n-1):
    if l[i+1]>l[i]:
        c+=1
        if max<c:
            max=c
    else:
        c=1
print(max)