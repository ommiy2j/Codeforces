n=int(input())
a=[]
for i in range(n):
    x=[]
    for i in range(n):
        x.append(int(input()))
    a.append(x)

for i in range(n):
    m=min(a[i])
    index=a[i].index(m)
    max=m
    for i in range(n):
        if a[i][index]>max:
            max=a[i][index]
    if max==m:
        print(m)
        c=1
    else:
        c=0
if c==0:
    print("Invalid input")