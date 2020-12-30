class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=[]
        for i in nums1:
            a.append(i)
        for i in nums2:
            a.append(i)
        a.sort()
        if(len(a)%2==0):
            x,y=len(a)//2,(len(a)//2)+1
            m=(a[x-1]+a[y-1])/2
        else:
            x=(len(a)+1)//2
            m=a[x-1]

        
        return m