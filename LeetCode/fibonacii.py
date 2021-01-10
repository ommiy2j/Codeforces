n=int(input())
temp=[-1 for i in range(n+1)]
temp[0]=1
temp[1]=1
if n>=2:
    for i in range(2,n+1):
        temp[i]=temp[i-1]+temp[i-2]
    print(temp[-1])
elif n==1 or n==0:
    print(temp[0])
    