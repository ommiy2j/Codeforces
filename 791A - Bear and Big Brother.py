a,b=map(int,input().split())
c=0
x=a
y=b
while(a<=b):
    a+=2*a
    b+=b
    c+=1
print(c)