for i in range(int(input())):
    n=int(input())
    seive=[1 for i in range(9000000)]
    seive[0]=0
    seive[1]=0
    i=2
    while(i*i<=9000000):
        if(seive[i]):
            for j in range(i*i,9000000,i):
                seive[j]=0
        i+=1
    i=0
    c=0
    for i in range(9000000):
        if(seive[i]):
            c+=1
            if c==n:
                print(i)
                break
    
        