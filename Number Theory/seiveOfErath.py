n=int(input())
seive=[1 for i in range(n+1)]
seive[0]=0
seive[1]=0
i=2
while(i*i<=n):
    if(seive[i]):
        for j in range(i*i,n+1,i):
            seive[j]=0
    i+=1
print(seive)