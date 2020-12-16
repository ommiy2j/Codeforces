n=int(input())
s=n//5
if(n>5 and n%5!=0):
    s+=1
elif(n%5==0 and n>5):
    s=s
else:
    s=1
print(s)
    

    