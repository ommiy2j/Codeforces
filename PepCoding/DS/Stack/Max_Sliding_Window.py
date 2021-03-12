class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        # n=int(input())
        # a=[int(i) for i in input().split()]
        # k=int(input())
        n=len(a)
        stack=[]
        t=[0 for i in range(n)]
        t[-1]=len(a)
        stack.append(len(a)-1)
        for i in range(n-2,-1,-1):
            while len(stack)>0 and a[stack[-1]] <= a[i]:
                stack.pop()
            if len(stack)>0:
                t[i]=stack[-1]
            else:
                t[i]=len(a)
            stack.append(i)
        x=[]
        for i in range(len(a)-k+1):
            j=i
            while(t[j]<i+k):
                j=t[j]
            x.append(a[j])
        return x
        