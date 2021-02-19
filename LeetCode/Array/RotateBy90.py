class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(a)
        for i in range(n):
            for j in range(n-1,i,-1):
                a[i][j],a[j][i]=a[j][i],a[i][j]
        for i in range(n):
            a[i].reverse()


# Your input
# [[1,2,3],[4,5,6],[7,8,9]]
# Output
# [[7,4,1],[8,5,2],[9,6,3]]
# Expected
# [[7,4,1],[8,5,2],[9,6,3]]