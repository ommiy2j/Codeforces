for i in range(int(input())):
    n,k=map(int,input().split())
    k-=1
    if n%2==0:
        print((k%n)+1)
    else:
        mid=n//2
        ans=((k//mid)+k)%n
        print(ans+1)