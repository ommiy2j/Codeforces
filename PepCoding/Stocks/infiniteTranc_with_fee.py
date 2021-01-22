n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
tax=int(input())
bsp=[0 for i in range(n)]
ssp=[0 for i in range(n)]
bsp[0]=-l[0]
for i in range(1,n):
    x=ssp[i-1]-l[i]
    if x>bsp[i-1]:
        bsp[i]=x
    else:
        bsp[i]=bsp[i-1]
    if (l[i]-tax+bsp[i-1])>ssp[i-1]:
        ssp[i]=l[i]-tax+bsp[i-1]
    else:
        ssp[i]=ssp[i-1]
print(max(ssp))