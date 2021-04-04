n=int(input())
if(n%2==0):
    noOfPosdigits=n//2
else:
    noOfPosdigits=(n-1)//2
noOfNegdigits=n-noOfPosdigits
posSum=noOfPosdigits*(noOfPosdigits+1)
negSum=noOfNegdigits**2

print(posSum-negSum)