import math
for i in range(int(input())):
    n=int(input())
    if(n<3):
        print(0)
    else:
        c=0
        a=int(math.sqrt(2*n-1))
        print((a-1)//2)