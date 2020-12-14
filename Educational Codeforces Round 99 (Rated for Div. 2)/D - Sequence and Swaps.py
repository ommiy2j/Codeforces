def check(arr):
    newarr=[]
    for i in range(1,len(arr)):
        if(arr[i-1]>arr[i]):
            return False
    return True


t=int(input())
for i in range(t):
    n,x=input().split()
    n=int(n)
    x=int(x)
    a=[int(i)for i in input().split()]
    j=0
    c=0
    while(j<n):
        if(check(a)):
            break
        if(a[j]>x):
            a[j],x=x,a[j]
            c+=1
        
        j+=1
    z=[]
    for i in a:
        z.append(i)
    z.sort()
    c1=0
    for i in range(len(a)):
        if(a[i]==z[i]):
            c1+=1
    if(c1==len(a)):
        pass
    else:
        c=-1
    print(c)
    

            