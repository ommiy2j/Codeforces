def sumOfAp(n):
    s=(2+(n-1)*2)*(n/2)
    return s
n=int(input())

s=sumOfAp(n)+sumOfAp(n-1)
print(int(s))