#election is conducted in a town with n population. every person casts a vote for a candidate. later,it is relaised that only votes cast by people aged above 18 and 18 should bw considered. which candidate wins when valid votes are included. if no winner can be decided due to tie or no valid votes then print -1. given array vote[] and age[]
# eg:
# 5
# 1 2 1 3 2
# 17 21 20 19 18
# op:2

n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
d={}
for i in range(len(vote)):
    if age[i]>=18:
        j=vote[i]
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
ele=-1
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        ele=i
print(ele)