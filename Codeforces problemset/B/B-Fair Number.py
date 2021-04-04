def solve(n):
    while(True):
        n1=n
        while(n1):
            r=n1%10
            if r!=0 and n%r!=0:
                break
            n1//=10
        if n1==0:
            return n
        n+=1
        
        
for i in range(int(input())):
    n=int(input())
    print(solve(n))