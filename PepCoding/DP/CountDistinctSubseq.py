s=input()
t=[0 for i in range(len(s)+1)]
t[0]=1
if len(set(list(s)))==len(s):
    print((2**len(s))-1)
else:
    for i in range(1,len(s)+1):
        t[i]=t[i-1]*2
        for j in range(i-1,-1,-1):
            if s[i-1]==s[j-1]:
                t[i]=t[i]-t[j-1]
                break
    print(t[-1] - 1)
    


#abc=8
#abcbac=50
