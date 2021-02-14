for i in range(int(input())):
    s=input()
    if (len(s)%2!=0) or s[0]==')' or s[-1]=='(':
        print("NO")
    else:
        print("YES")
        