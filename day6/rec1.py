# n=5
# 5 4 3 2 1
def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
n=5
fun(n)