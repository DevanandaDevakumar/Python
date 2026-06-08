# n=10
# 10 8 6 4 2
# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-2)
# n=10
# fun(n)

def fun(n):
    if n==0:
        return
    if n%2==0:
        print(n,end=" ")
    fun(n-1)
n=10
fun(n)