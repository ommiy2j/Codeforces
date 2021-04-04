class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')' and not stack:
                c+=1
            elif i==')' and stack:
                stack.pop()
        # print(stack,c)
        return len(stack)+c