# After the lessons n groups of schoolchildren went outside and decided to visit Polycarpus
# to celebrate his birthday. We know that the i-th group consists of si friends (1 ≤ si ≤ 4),
#  and they want to go to Polycarpus together. They decided to get there by taxi. Each car can
#  carry at most four passengers. What minimum number of cars will the children need if all members
#  of each group should ride in the same taxi
# (but one taxi can take more than one group)?

#Input
# 5
# 1 2 4 3 3

#op
#4


n=int(input())
a=[int(i) for i in input().split()]
t=[0 for i in range(1,5)]
for i in a:
    if i==1:
        t[0]+=1
    elif i==2:
        t[1]+=1
    elif i==3:
        t[2]+=1
    else:
        t[3]+=1

ans=t[3]+t[2]+t[1]//2
t[0]=t[0]-t[2]
if t[1]%2==1:
    ans+=1
    t[0]-=2
if t[0]>0:
    ans+=(t[0]+3)//4
print(t,ans)