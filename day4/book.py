# find max cost such that its of k consequtive books 
# sliding window approach
# l=list(map(int,input().split()))
# k=int(input())
# max=0
# for i in range(len(l)-k+1):
#     s=sum(l[i:i+k])
#     if s>max:
#         max=s
# print(max)

# l=list(map(int,input().split()))
# k=int(input())
# max1=0
# for i in range(len(l)-k+1):
#     sum=0
#     for j in range(i,i+k):
#         sum=sum+l[j]
#     max1=max(sum,max1)
# print(max1)

# 2 3 1 5 2 4 6 7 8 5 2 2 3
# 3

# SLIDING WINDOW APPROACH
# l=list(map(int,input().split()))
# k=int(input())
# sum=sum(l[:k])
# max1=sum
# for i in range(1,len(l)-k+1):
#     sum=sum-l[i-1]+l[i+k-1]
#     max1=max(sum,max1)
# print(max1)

l = list(map(int, input().split()))
k = int(input())
curr = sum(l[:k])
max_sum = curr
for i in range(k, len(l)):
    curr = curr - l[i - k] + l[i]
    max_sum = max(max_sum, curr)
print(max_sum)