n=int(input())
a=input()
lst=[]
for i in a:
    if i.lower() not in lst:
        lst.append(i.lower())
 
if(len(lst)>=26):
    print("YES")
else:
    print("NO")