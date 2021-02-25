a=[]
for i in range(4):
    x=[i for i in input().split()]
    a.append(x)
new=[[0 for i in range(len(a))] for j in range(len(a))]
for j in range(len(a[0])):
    for i in range(len(a)-1,-1,-1):
        new[j][len(a)-i-1]=a[i][j]
print(new)