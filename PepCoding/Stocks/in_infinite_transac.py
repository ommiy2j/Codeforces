n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
b=0
s=0
profit=0
m=0
for i in range(1,n):
    if l[i]>=l[i-1]:
        s+=1
    else:
        profit+=l[s]-l[b]
        b=i
        s=i
profit+=l[s]-l[b]
print(profit)
    