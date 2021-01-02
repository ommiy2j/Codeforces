def longestPalindromeSubsequence(s):
    a=len(s)
    t=[[0 for i in range(a)] for i in range(a)]
    for i in range(a):
        t[i][i]=1
    for subString in range(2,a+1):
        for row in range(0,a - subString + 1):
            col=row+subString-1
            if s[row]==s[col]:
                if a==2:
                    t[row][col]=2
                else:
                    t[row][col]=2+t[row+1][col-1]
            else:
                t[row][col]=max(t[row+1][col],t[row][col-1])
    return t[0][-1]

a='agbdba'
print(longestPalindromeSubsequence(a))
