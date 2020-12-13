t=int(input())
for i in range(t):
     n,k=input().split()
     n,k=int(n),int(k)
     ans=''
     for j in range(k):
         ans+='a'
     other='bca'
     diff=n-k
     for k in range(diff):
         ans+=other
     print(ans[0:n])
    
