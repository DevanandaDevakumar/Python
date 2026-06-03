#election is conducted in a town with n population. every person casts a vote for a candidate. later,it is relaised that only votes cast by people aged above 18 and 18 should bw considered. which candidate wins when valid votes are included. if no winner can be decided due to tie or no valid votes then print -1. given array vote[] and age[]
# eg:
# 5
# 1 2 1 3 2
# 17 21 20 19 18
# op:2

# This code is not working for -1 condn
# n=int(input())
# vote=list(map(int,input().split()))
# age=list(map(int,input().split()))
# c=[0]*max(vote)
# for i in range(n):
#     if age[i]>=18:
#         j=vote[i]-1
#         c[j]+=1
# print(c)
# max=0
# ele=-1
# for i in c:
#     if c[i]==max:
#         ele=(-1)
#     elif c[i]>max:
#         max=c[i]
#         ele=i+1
# print(ele)


# This will work
# n=int(input())
# vote=list(map(int,input().split()))
# age=list(map(int,input().split()))
# c=[0]*max(vote)
# for i in range(n):
#     if age[i] >= 18:
#         c[vote[i]-1] += 1
# mx = max(c)
# if mx == 0:
#     print(-1)
# else:
#     if c.count(mx) > 1:   # tie
#         print(-1)
#     else:
#         print(c.index(mx) + 1)

n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
c=[0]*max(vote)
for i in range(n):
    if age[i] >= 18:
        c[vote[i]-1] += 1
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0])+1)

#segment tree asked for higher lpa