n,m=[int(i) for i in input().split()]
if(n%2==0):
    noOfOdd=n//2
    noOfEven=n//2
else:
    noOfOdd=(n+1)//2
    noOfEven=(n-1)//2
if(m>noOfOdd):
    e=m-noOfOdd
    reqNo=2+(e-1)*2
else:
    reqNo=1+(m-1)*2
print(reqNo)
    