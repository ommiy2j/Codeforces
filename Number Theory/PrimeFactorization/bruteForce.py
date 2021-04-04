n=int(input())
for i in range(2,n+1):
    if (n%i==0):
        c=0
        while(n%i==0):
            c+=1
            n//=i
        print('('+str(i)+'^'+str(c)+')',end='')
        