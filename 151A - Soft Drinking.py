n, k, l, c, d, p, nl, np=map(int,input().split())
tm=(k*l)//n
lime=c*d
s=p//np
ans=min(tm,lime,s)//n
print(ans)