# right rot.
# n=int(input())
# a=list(map(int,input().split()))
# k=int(input())%n
# res=[0]*n
# for i in range(n):
#     j=(i+k)%n
#     res[j]=a[i]
# print(res)

# using function
# a=[1,2,3,4,5,6,7]
# n=len(a)
# k=int(input())%n
# def rotate(i,j):
#     while(i<j):
#         a[i],a[j]=a[j],a[i]
#         i+=1
#         j-=1
# rotate(0,n-1)
# rotate(0,k-1)
# rotate(k,n-1)
# print(a)

# left rot
# 1 2 3 4 5 6 7
# op: 4 5 6 7 1 2 3
# how to
# 3 2 1 4 5 6 7
# 3 2 1 7 6 5 4
# 4 5 6 7 1 2 3

# using slice op
# n = int(input())
# a = list(map(int, input().split()))
# k = int(input()) % n
# res = a[k:] + a[:k]
# print(res)

# without rotate
# n = int(input())
# a = list(map(int, input().split()))
# k = int(input()) % n
# res = []
# for i in range(k, n):
#     res.append(a[i])
# for i in range(k):
#     res.append(a[i])
# print(res)

# with rotate
# n = int(input())
# a = list(map(int, input().split()))
# k = int(input()) % n
# res = []
# for i in range(k - 1, -1, -1):
#     res.append(a[i])
# for i in range(n - 1, k - 1, -1):
#     res.append(a[i])
# res = list(reversed(res))
# print(res)

# using function
# a=[1,2,3,4,5,6,7]
# n=len(a)
# k=int(input())%n
# def rotate(i,j):
#     while(i<j):
#         a[i],a[j]=a[j],a[i]
#         i+=1
#         j-=1
# rotate(0,k-1)
# rotate(k,n-1)
# rotate(0,n-1)
# print(a)