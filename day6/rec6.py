# n=5
# 1 2 3 4 5 4 3 2 1
# def rec(n,i=1):
#     if i>n:
#         return
#     print(i,end=" ")
#     rec(n,i+1)
#     if i!=n:
#         print(i,end=" ")
# rec(5)

def rec(n,i=1):
    if i==n:
        print(i,end=" ")
        return
    print(i,end=" ")
    rec(n,i+1)
    print(i,end=" ")
rec(5)