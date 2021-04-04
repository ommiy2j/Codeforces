n=input()
u=0
l=0
for i in n:
    if i.isupper():
        u+=1
    else:
        l+=1
if(l>=u):
    print(n.lower())
else:
    print(n.upper())