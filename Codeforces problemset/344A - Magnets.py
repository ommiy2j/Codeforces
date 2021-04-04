n=int(input())
s=""
for i in range(n):
    s+=input()
c=0
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        c+=1
print(c+1)