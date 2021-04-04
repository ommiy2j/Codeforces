n=int(input())
ny=n+1
if(len(set(str(ny)))==len(list(str(ny)))):
    print(ny)
else:
    i=0
    while(len(set(str(ny)))!=len(list(str(ny)))):
        ny+=1
    print(ny)
    