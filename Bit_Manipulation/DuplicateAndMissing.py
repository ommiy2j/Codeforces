n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
xor=0
for i in a:
    xor^=i
for i in range(1,len(a)+1):
    xor=xor^i
rsb=xor & (-xor)
x=0
y=0
for i in a:
    if  ((i & rsb)==0):
        x=x^i
    else:
        y=y^i
for i in range(1,len(a)+1):
    if  (i & rsb)==0:
        x=x^i
    else:
        y=y^i
if x in a:
    print('Missing Number -> '+str(y))
    print('Repeating Number -> '+str(x))
elif y in a:
    print('Missing Number -> '+str(x))
    print('Repeating Number -> '+str(y))