class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        news=''
        for i in s:
            if i=='(':
                c+=1
                if c>1:
                    news+=i
            elif i==')':
                c-=1
                if c>0:
                    news+=i
        return news
                    