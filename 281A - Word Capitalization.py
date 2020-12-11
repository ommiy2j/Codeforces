n=input()
a=n[0]
if(n[0].islower()):
    a=a.upper()
news=a
for i in range(1,len(n)):
    news+=n[i]
print(news)