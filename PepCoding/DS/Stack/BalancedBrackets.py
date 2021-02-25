s=input()
stack=[]
top=-1
c=0
for i in range(len(s)):
    if s[i] in ['(','[','{']:
        stack.append(s[i])
        top+=1
    elif s[i]==')':
        if len(stack)==0:
            print('false')
            c=1
            break
        elif stack[top]!='(':
            print('false')
            c=1
            break
        else:
            stack.pop()
            top-=1
    elif s[i]==']':
        if len(stack)==0:
            print('false')
            c=1
            break
        elif stack[top]!='[':
            print('false')
            c=1
            break
        else:
            stack.pop()
            top-=1
    elif s[i]=='}':
        if len(stack)==0:
            print('false')
            c=1
            break
        elif stack[top]!='{':
            print('false')
            c=1
            break
        else:
            stack.pop()
            top-=1
if c==0:
    if len(stack)==0:
        print('true')
    else:
        print('false')
        