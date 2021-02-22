class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1 or len(nums)==2:
            return 1
        n=len(nums)
        prevdiff=0
        r=1
        for i in range(1,n):
            d=nums[i]-nums[i-1]
            if (d>0 and prevdiff<=0) or (d<0 and prevdiff>=0):
                r+=1
                prevdiff=d
        return r