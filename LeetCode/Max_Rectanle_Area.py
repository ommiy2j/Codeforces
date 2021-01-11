class Solution:
    def histogram(self,l):
        stack=[]
        i=0
        top=0
        maxA=0
        while(i<len(l)):
            if len(stack)==0 or l[top]<=l[i]:
                stack.append(i)
                top=i
                i+=1
            else:
                temp=stack[-1]
                stack.pop()
                if (len(stack)==0):
                    a=l[temp]*i
                else:
                    a=l[temp]*(i-stack[-1]-1)
                    top-=1
                if a>maxA:
                    maxA=a
        while(len(stack)!=0):
            temp=stack[-1]
            stack.pop()
            if (len(stack)==0):
                a=l[temp]*i
                top-=1
            else:
                a=l[temp]*(i-stack[-1]-1)
                top-=1
            if a>maxA:
                maxA=a
        return maxA
    def maximalRectangle(self, m: List[List[str]]) -> int:
        if len(m)==0:
            return 0
        temp=[]
        maxA=0
        for i in range(len(m[0])):
            temp.append(int(m[0][i]))
        c=0
        maxT=0
        if len(m)==1:
            for i in temp:
                if i==1:
                    c+=1
                    if c>maxT:
                        maxT=c
                else:
                    c=0
            return maxT
        for i in range(1,len(m)):
            for j in range(len(m[i])):
                if int(m[i][j])==1:
                    temp[j]+=1
                else:
                    temp[j]=0
            x=self.histogram(temp)
            if x>=maxA:
                maxA=x
                    
        return maxA