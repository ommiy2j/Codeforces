class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        news=''
        for i in stack:
            news+=i
        return news



# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".