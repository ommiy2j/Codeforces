class Solution:
    def maximalSquare(self, m: List[List[str]]) -> list:
        t=[[0 for i in range(len(m[0]))] for j in range(len(m))]
        c=0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]=='1':
                    t[i][j]=min(t[i-1][j],t[i][j-1],t[i-1][j-1]) + 1
                    if c<t[i][j]:
                        c=t[i][j]
        return c*c