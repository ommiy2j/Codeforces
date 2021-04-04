for i in range(int(input())):
    n=int(input())
    c=1
    while(n>1):
        i=2
        while(i*i<=n):
            if n%i==0:
                n//=i
                c+=1
                break
            i+=1
        c+=1
        break
    if c%2==0:
        print('Divesh')
    else:
        print('Tanya')