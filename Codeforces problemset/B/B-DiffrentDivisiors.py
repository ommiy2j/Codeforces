prime=[]
def isPrime():
    global prime
    seive=[1 for i in range(100000+1)]
    seive[0]=0
    seive[1]=0
    i=2
    while(i*i<=100000):
        if seive[i]:
            for j in range(i*i,100000+1,i):
                seive[j]=0
        i+=1
    prime=[]
    for i in range(100000+1):
        if seive[i]:
            prime.append(i)


for i in range(int(input())):
    isPrime()
    d=int(input())
    for i in range(len(prime)+1):
        if prime[i]-1 >= d:
            fno=prime[i]
            break
    for i in range(len(prime)+1):
        if (prime[i]-fno) >= d:
            sno=prime[i]
            break
    print(fno*sno)
