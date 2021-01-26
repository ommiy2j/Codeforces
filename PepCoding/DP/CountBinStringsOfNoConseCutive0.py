n=int(input())
t0=[0 for i in range(n+1)]
t1=[0 for i in range(n+1)]
OldcountZeros=1
OldcountOnes=1
for i in range(2,n+1):
    newCountZeros=OldcountOnes
    newCountones=OldcountOnes+OldcountZeros
    OldcountZeros=newCountZeros
    OldcountOnes=newCountones
print(newCountZeros+newCountones)



#method 2

n=int(input())
t0=[0 for i in range(n+1)]
t1=[0 for i in range(n+1)]
t1[1] = 1
t0[1]=1
for i in range(2, n + 1):
    t1[i] = t1[i - 1] + t0[i - 1]
    t0[i]=t1[i-1]
print(t1[-1]+t0[-1])