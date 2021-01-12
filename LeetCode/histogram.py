class Solution:
    def largestRectangleArea(self, l: List[int]) -> int:
        stack=[]
        i=0
        top=0
        maxA=0
        while(i<len(l)):
            if len(stack)==0 or l[stack[-1]]<=l[i]:
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
            
    

        
        
        
        