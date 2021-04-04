n=int(input())
max=0
for i in range(n):
    a,b=map(int,input().split())
    if(i==0):
        passInside=a
        passEnter=b
        totalpass=passInside+passEnter
        #print(totalpass,passEnter)
        if(max<=totalpass):
            max=totalpass
    elif (i==1):
        passExit=a
        passInside=passEnter-a
        passEnter=b
        totalpass=passInside+passEnter
        #print(totalpass,passEnter)
        if(max<=totalpass):
            max=totalpass
    else:
        passExit=a
        passInside=totalpass-a
        passEnter=b
        totalpass=passInside+passEnter
        #print(totalpass,passEnter)
        if(max<=totalpass):
            max=totalpass
        
            
print(max)