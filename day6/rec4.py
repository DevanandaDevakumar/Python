# n=10
# 2 4 6 8 10
# def fun(n):
#     if n==0:
#         return
#     fun(n-2)
#     print(n,end=" ")
# n=10
# fun(n)

def fun(n):
    if n==0:
        return
    fun(n-1)
    if n%2==0:
        print(n,end=" ")
n=10
fun(n)