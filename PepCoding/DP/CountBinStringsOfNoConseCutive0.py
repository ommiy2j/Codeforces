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