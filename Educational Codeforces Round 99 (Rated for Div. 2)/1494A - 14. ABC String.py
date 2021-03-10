for i in range(int(input())):
    s=input()
    if(s[0]==s[-1]):
        print("NO")
    else:
        c=0
        x=0
        op=s[0]
        cl=s[-1]
        stack=[]
        for i in range(len(s)):
            if s[i]==op:
                stack.append(s[i])
            else:
                if(len(stack)!=0):
                    stack.pop()
                else:
                    x=1
                    break
        if len(stack)==0 and x==0:
            c=1
        x=0
        stack=[]
        for i in range(len(s)):
            if s[i]==op or s[i]!=cl:
                stack.append(s[i])
            else:
                if(len(stack)!=0):
                    stack.pop()
                else:
                    x=1
                    break
        
        if len(stack)==0 and x==0:
            c=1
        if c==1:
            print("YES")
        else:
            print("NO")

                  

#    i / p == AABBAC
#    In the first testcase one of the possible strings b is "(())()".