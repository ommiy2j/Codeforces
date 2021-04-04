n=int(input())
lst=[int(i) for i in input().split()]
min=lst[0]
max=lst[0]
c=0
for i in range(n):
    if(lst[i]>max):
        max=lst[i]
        c+=1
    elif(lst[i]<min):
        min=lst[i]
        c+=1
    else:
        pass
print(c)
    