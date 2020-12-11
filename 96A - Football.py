n=input()
c=0
for i in range(len(n)):
    s=0
    x=i+7
    if(x>len(n)):
            break
    else:
        for j in range(i,x):
            
            s=s+int(n[j])
        if(s==0 or s>6):
           c+=1
if(c>0):
    print("YES")
else:
    print("NO")