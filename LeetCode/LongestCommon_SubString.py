class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        t=[[0 for i in range(len(A)+1)] for i in range(len(B)+1)]
        c=0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1]:
                    t[i][j]=t[i-1][j-1]+1
                    if t[i][j]>c:
                        c=t[i][j]
        return c
        