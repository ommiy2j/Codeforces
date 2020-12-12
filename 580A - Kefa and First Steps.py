n=int(input())
lst=[int(i) for i in input().split()]
c=1
max=0
for i in range(n-1):
    if(lst[i]>lst[i+1]):
        if(c>max):
            max=c
        c=1
    else:
        c+=1
    
if(c>max):
    max=c
print(max)
        
