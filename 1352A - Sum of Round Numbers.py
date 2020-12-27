for i in range(int(input())):
    n=input()
    s=[]
    for i in range(len(n)):
        if n[i] !=0:
            s.append(int(n[i])*(10**(len(n)-i-1)))
    c=0
    for i in s:
        if i!=0:
            c+=1
    print(c)
    for i in s:
        if i!=0:
            print(i,end=' ')
    print()