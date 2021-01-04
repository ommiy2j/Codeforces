def powerOfTwo(n):
    i = 1
    while (i*2 <= n):
        i = i * 2
    return i


def solution(n):
    hp2 = powerOfTwo(n)
    l = n - hp2;
    return 2 * l + 1


n = int(input())
print(solution(n))
