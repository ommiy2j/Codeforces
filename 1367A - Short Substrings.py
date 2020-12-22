for i in range(int(input())):
    n=input()
    i=0
    s=''
    while(i<len(n)-1):
        if(n[i]==n[i+1]):
            s+=n[i+1]
            i+=1
        else:
            s+=n[i]
        i+=1
    print(s+n[-1])