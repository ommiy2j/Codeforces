def subSeq(s):
    if len(s)==0:
        return [""]
    c=s[0]
    ros=s[1:]
    res=subSeq(ros)
    l=[]
    for i in res:
        l.append(""+i)
    for i in res:
        l.append(c+i)
    return l
s=input()
l=subSeq(s)
l=','.join(map(str,l))
print(l)




#Sample Input
# abc
# Sample Output
# [, c, b, bc, a, ac, ab, abc]