class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
                # print(stack)
            elif len(stack)>0:
                if i.lower()==stack[-1] and i.isupper() and stack[-1].islower():
                    stack.pop()
                elif i.upper()==stack[-1] and i.islower() and stack[-1].isupper():
                    stack.pop()
                else:
                    stack.append(i)
                    # print(stack)
                    
        print(stack)
        return ''.join(stack)



#         Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
# Example 2:

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:

# Input: s = "s"
# Output: "s"