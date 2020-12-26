for i in range(int(input())):
    n=input()
    l=[1,2,3,4,5,6,7,8,9]
    for i in l:
        if i==int(n[0]):
            a=l.index(i)+1
    a=(10*(a-1))
    if(len(n)==1):
        a+=1
    elif(len(n)==2):
        a+=3
    elif(len(n)==3):
        a+=6
    else:
        a+=10
    print(a)