n,t=input().split()
n,t=int(n),int(t)
s=list(input())
for i in range(t):
    j=0
    while(j<n-1):
        if(s[j]=='B' and s[j]!=s[j+1]):
            s[j+1],s[j]=s[j],s[j+1]
            j+=2
        elif(s[j]==s[j+1]):
            j+=1
        else:
            j+=1
s=''.join(s)
print(s)
        