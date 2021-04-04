class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=''
        for i in s:
            stack+=i
            if len(stack)>=k:
                if stack[-k:]==i*k:
                    stack=stack[:-k]
        return stack
                    


# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"