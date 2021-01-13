class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        t=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    t[i]=max(t[i],t[j]+1)
        return max(t)
                