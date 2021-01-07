n=int(input())
flag= False 
j=0
rev=0
for i in range(32,-1,-1):
    mask=(1<<i)
    if(flag):
        if (n&mask)!=0:
            print(1,end='')
            smask=(1<<j)
            rev|=smask
        else:
            print(0,end='')
        j+=1
    else:
        if (n&mask)!=0:
            flag=True
            print(1,end='')
            smask=(1<<j)
            rev|=smask
            j+=1
print()
print(rev)
        
        