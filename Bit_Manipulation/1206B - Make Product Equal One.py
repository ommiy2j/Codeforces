n=int(input())
l=[int(i) for i in input().split()]
c=0
neg=[]
z=0
for i in l:
    if i<0:
        neg.append(i)
    elif i==0:
        z+=1
neg.sort(reverse=True)
for i in range(len(neg)):
    if neg[i]==-1:
        pass
    else:
        c+=abs(neg[i])-1
        neg[i]=neg[i]+(abs(neg[i])-1)
if len(neg)%2!=0:
    if z==0:
        c+=2
    else:
        if z>len(neg):
            for i in range(len(neg)):
                neg[i]=neg[i]+(abs(neg[i]))
                c+=1
            c+=z-len(neg)
        else:
            for i in range(z):
                neg[i]=neg[i]+(abs(neg[i]))
                c+=1
else:
    c+=z
for i in l:
    if i>1:
        c+=i-1
print(c)
            
        
    