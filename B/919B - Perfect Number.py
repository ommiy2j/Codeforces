def sumOfDigits(n):
    s=0
    while(n):
        s+=n%10
        n//=10
    return s
n=int(input())
i=19
j=1
while(j<n):
    i+=9
    if sumOfDigits(i)==10:
        j+=1
print(i)