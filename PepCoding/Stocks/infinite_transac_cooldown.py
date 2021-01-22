n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
bsp=[0 for i in range(n)]
ssp=[0 for i in range(n)]
csp=[0 for i in range(n)]
bsp[0]=-l[0]
for i in range(1,n):
    nbsp=csp[i-1]-l[i]
    if nbsp>bsp[i-1]:
        bsp[i]=nbsp
    else:
        bsp[i]=bsp[i-1]
    nssp=l[i]+bsp[i-1]
    if nssp>ssp[i-1]:
        ssp[i]=nssp
    else:
        ssp[i]=ssp[i-1]
    ncsp=ssp[i-1]
    if ncsp>csp[i-1]:
        csp[i]=ncsp
    else:
        csp[i]=csp[i-1]
print(max(ssp))