class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        t=[[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
        m=0
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 or j==0:
                    t[i][j]=0
                elif s1[i-1]==s2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
            m=max(m,t[i][j])
        return(t[len(s1)][len(s2)])