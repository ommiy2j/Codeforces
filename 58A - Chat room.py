n=input()
s='hello'
j=0
c=0
for i in range(len(n)):
    if(n[i]==s[j]):
        j+=1
        c+=1
        if(c==5):
            break
if(c==5):
    print("YES")
else:
    print("NO")
        
        