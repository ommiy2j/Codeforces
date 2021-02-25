stack=[]
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
t=[0 for i in range(n)]
t[-1]=-1
stack.append(a[-1])
top=0
i=n-1

for i in range(n-2,-1,-1):
    while(len(stack)>0 and stack[top]<=a[i]):
        stack.pop()
        top-=1
    if(len(stack)>0):
        t[i]=stack[top]
    else:
        t[i]=-1
    stack.append(a[i])
    top+=1
for i in t:
    print(i)
        
            