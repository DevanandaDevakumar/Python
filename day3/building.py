#no of buildings get sunlight. n has height of buildings starting from close to sun to farther away
n=map(int,input().split())
h=0
s=0
for i in n:
    if i>h:
        h=i
        s=s+1
print(s)

# find max in a list
# n=0
# for i in l:
#     m=max(n,i)

