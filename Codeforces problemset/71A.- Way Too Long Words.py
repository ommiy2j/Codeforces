n=int(input())
for i in range(n):
    w=input()
    if(len(w)>10):
        s=w[0]
        l=w[-1]
        num=len(w)-2
        newword=s+str(num)+l
        print(newword)
    else:
        print(w)