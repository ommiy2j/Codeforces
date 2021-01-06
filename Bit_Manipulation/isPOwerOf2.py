n=int(input())
rsbm=n&-n
c=0
while(n!=0):
    n-=rsbm
    rsbm=n&-n
    c+=1
if c==1:
    print('true')
else:
    print('false')


# 2nd Method

def ispOwerOf2(n):
    if n & (n - 1) == 0:
        print('true')
    else:
        print('false')