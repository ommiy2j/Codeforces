a=int(input())
b=int(input())
c=int(input())
if(a==1 and c==1):
    print(2+b)
elif(a==1):
    print((a+b)*c)
elif(b==1):
    print(max((a+b)*c,a*(b+c)))
elif(c==1):
    print(a*(b+c))
else:
    print(a*b*c)
