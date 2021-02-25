class Solution:
    def reverse(self,a,i,j):
        while(i<j):
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-1-k)
        self.reverse(nums,len(nums)-k,len(nums)-1)
        self.reverse(nums,0,len(nums)-1)
    