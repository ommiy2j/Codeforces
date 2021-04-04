n=int(input())
c=0
for i in range(n):
    a=input()
    if(a=='X++' or a=='++X'):
        c+=1
    else:
        c-=1
print(c)