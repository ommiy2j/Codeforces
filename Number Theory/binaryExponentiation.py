b=2
power=5
res=1
while(power!=0):
    if power%2==0:
        b=b**2
        power//=2
    else:
        res*=b
        power-=1
print(res)