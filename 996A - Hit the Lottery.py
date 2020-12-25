n=int(input())
c = [1,5,10,20,100] 
c=0
while(n!=0):
    if(n>=100):
        c+=n//100
        n=n%100
    elif(n>=20):
        c+=n//20
        n=n%20
        
    elif n>=10:
        c+=n//10
        n=n%10
    elif n>=5:
        c+=n//5
        n=n%5
    else:
        c+=n//1
        n=0

print(c)