n = int(input())
a = [0] * 3

for i in range(n):
    b = [int(x) for x in input().split()]
    for j in range(3):
        a[j] += b[j]
        print(a[j])

ans = [x for x in a if x == 0]
print('YES' if len(ans) == 3 else 'NO')