def subsetSum(a,sum):
        t=[[0 for i in range(sum+1)] for i in range(len(a))]
        for i in range(len(a)):
            t[i][0]=1
        for i in range(len(a)):
            for j in range(sum+1):
                if a[i]==j or t[i-1][j]==1 or t[i-1][j-a[i]]==1:
                    t[i][j]=1
        return t[len(a)-1][sum]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        elif len(nums)==1:
            return False
        elif max(nums)>sum(nums)//2:
            a=sum(nums)-max(nums)
            if(a==max(nums)):
                return True
            else:
                False
        else:
            a=sum(nums)//2
            nums.sort()
            x=subsetSum(nums,a)
            if x==1:
                return True
            else:
                return False
    
        