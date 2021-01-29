def printSubSS(s,ans=""):
    if len(s)==0:
        print(ans)
        return
    ch=s[0]
    sub=s[1:]
    printSubSS(sub,ans+ch)
    printSubSS(sub,ans)
    
    

s=input()
printSubSS(s,"")