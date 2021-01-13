class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        t=[]
        i=0
        ans=float('inf')
        if len(nums)==0:
            return 0
        while(i<len(nums)):
            j=i
            s1=0
            if nums[i]==s:
                    return 1
            else:
                while(j<len(nums)):
                    s1+=nums[j]
                    if s1>=s:
                        ans=min(ans,j-i+1)
                    j+=1
                i+=1
        if ans==float('inf'):
            return 0
        else:
            return ans
                
                    
                    
                