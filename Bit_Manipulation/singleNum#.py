class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s=nums[0]
        for i in range(1,len(nums)):
            s^=(nums[i])
        rsb=s&(~s+1)
        g1=0
        g2=0
        for i in range(len(nums)):
            if (nums[i]& rsb):
                g1^=nums[i]
            else:
                g2^=nums[i]
        return [g1,g2]
        