from math import ceil 
n,m,a=input().split()  
n,m,a=int(n),int(m),int(a)  
c=ceil(n/a)*ceil(m/a)  
print(c) 