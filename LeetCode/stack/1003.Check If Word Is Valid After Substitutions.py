class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<3:
            return False
        if s[0]=='c' or s[0]=='b':
            return False
        if s[-1]=='a' or s[-1]=='b':
            return False
        stack=[]
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i]=='c' and len(stack)>=2:
                if stack[-1]=='b':
                    stack.pop()
                else:
                    return False
                if stack[-1]=='a':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack)==0:
            return True
        return False