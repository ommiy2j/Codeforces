lst=[int(i) for i in input().split()]
d1=abs(lst[0]-lst[2])+abs(lst[0]-lst[1])
d2=abs(lst[1]-lst[2])+abs(lst[0]-lst[1])
d3=abs(lst[2]-lst[1])+abs(lst[0]-lst[2])
print(min(d1,d2,d3))