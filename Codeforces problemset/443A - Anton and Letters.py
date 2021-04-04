n=input()
lst=[]
for i in n:
    if i in lst:
        pass
    elif i==',' or i=='{' or i=='}' or i==' ':
        pass
    else:
        lst.append(i)
print(len(lst))