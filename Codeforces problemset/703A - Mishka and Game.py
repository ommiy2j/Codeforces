x,y=0,0
for i in range(int(input())):
    a,b=map(int,input().split())
    
    if a==b:
        x+=1
        y++1
    elif a>b:
        x+=1
    else:
        y+=1
if x>y:
    print("Mishka")
elif x==y:
    print("Friendship is magic!^^")
else:
    print("Chris")