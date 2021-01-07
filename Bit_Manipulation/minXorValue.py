n = int(input())
l = []
ans = []
for i in range(n):
    l.append(int(input()))
l.sort()
m=l[0]^l[1]
for i in range(1,n - 1):
    x = l[i] ^ l[i + 1]
    if x <= m:
        m=x
for i in range(n-1):
    if (l[i]^l[i+1])==m:
        ans.append(str(l[i])+', '+str(l[i+1]))
for i in ans:
    print(i)