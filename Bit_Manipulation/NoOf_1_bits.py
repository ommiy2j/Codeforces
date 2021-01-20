def hammingWeight(n):
        rsbm=n&(-n)
        c=0
        while(n):
            n=n-rsbm
            rsbm=n&(-n)
            c+=1
        return c
print(hammingWeight(5))