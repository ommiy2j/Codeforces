class Solution:
    def countTriplets(self, a: List[int]) -> int:
        c=0
        n=len(a)
        for i in range(n):
            val=a[i]
            for k in range(i+1,n):
                val=val^a[k]
                if val==0:
                    c+=k-i
        return c