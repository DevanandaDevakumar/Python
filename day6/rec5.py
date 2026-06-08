# n=5
# 5 4 3 2 1 2 3 4 5
def rec(n):
    if n==0:
        return
    print(n,end=" ")
    rec(n-1)
    if n!=1:
        print(n,end=" ")
rec(5)