l=[int(i) for i in input().split()]
l.sort()
a=l[-1]-l[-2]
b=l[-3]-a
c=l[0]-a
print(a,b,c)