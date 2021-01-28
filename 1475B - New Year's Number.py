for i in range(int(input())):
    n=int(input())
    if n<2020:
        print("NO")
    else:
        while(n>=2020):
            if n%2020:
                n-=2021
            else:
                n-=2020
        if n==0:
            print("YES")
        else:
            print("NO")
                
            
