w=input()
vowels=["A","O","Y","E","U","I",'a','o','y','e','u','i']
news=""
for i in w:
    if i in vowels:
        pass
    else:
        news+='.'+i
print(news.lower())