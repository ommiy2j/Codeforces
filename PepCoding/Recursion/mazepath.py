def getmazepath(sr,sc,dr,dc):
    if sc==dc and sr==dr:
        return [""]
    hpath=[]
    vpath=[]
    if sc<dc:
        hpath=getmazepath(sr,sc+1,dr,dc)
    if sr<dr:
        vpath=getmazepath(sr+1,sc,dr,dc)
    l=[]
    for i in hpath:
        l.append("h"+i)
    for i in vpath:
        l.append("v"+i)
    return l


n=int(input())
m=int(input())
paths=getmazepath(1,1,n,m)
print(paths)