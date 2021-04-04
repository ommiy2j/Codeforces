a=[]
for i in range(int(input())):
    a.append(input())
b=list(set(a))
if len(b)==1:
    print(b[0])
else:
    d=0
    c=0
    for i in a:
        if i==b[0]:
            c+=1
        else:
            d+=1
    if c>d:
        print(b[0])
    else:
        print(b[1])
