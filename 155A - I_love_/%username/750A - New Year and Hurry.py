n,k=input().split()
n,k=int(n),int(k)
t=0
c=0
totalTime=240-k
for i in range(1,n+1):
    t=t+(5*i)
    if(t<=totalTime):
        c+=1
    else:
        break

print(c)
