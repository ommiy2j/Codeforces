def hammingWeight(n):
        rsbm=n&(-n)
        c=0
        while(n!=0):
            n=n-rsbm
            rsbm=n&(-n)
            c+=1
        return c