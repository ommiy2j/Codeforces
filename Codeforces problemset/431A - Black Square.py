a,b,c,d=map(int,input().split())
s=input()
c1,c2,c3,c4=0,0,0,0
for i in s:
    if i=='1':
        c1+=1
    elif i=='2':
        c2+=1
    elif i=='3':
        c3+=1
    else:
        c4+=1
total=a*c1+b*c2+c*c3+d*c4
print(total)