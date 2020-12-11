n=input()
lst=[]
for i in n:
    if(i=="+"):
        pass
    else:
        lst.append(i)
lst.sort()
news=""
for i in range(len(lst)):
    if(i==len(lst)-1):
        news+=lst[i]
    else:
        news+=lst[i]+'+'
print(news)
        