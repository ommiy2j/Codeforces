def sol(n):
    if n==1:
        bres=[]
        bres.append('0')
        bres.append('1')
        return bres
    rres=sol(n-1)
    nres=[]
    for i in range(len(rres)):
        rstr=rres[i]
        nres.append("0"+rstr)
    i=len(rres)-1
    while(i>=0):
        rstr=rres[i]
        nres.append("1"+rstr)
        i-=1
    return nres
class Solution:
    def grayCode(self, n: int) -> List[int]:
        a=sol(n)
        l=[]
        for i in a:
            l.append(int(i,2))
        return l
            
        