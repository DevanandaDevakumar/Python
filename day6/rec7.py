# n=5
# 1 2 3 4 5 200
def fun(n):
    if n==0:
        return 200 
    i=fun(n-1)    
    print(n,end=" ")
    return i
n=5
print(fun(n))