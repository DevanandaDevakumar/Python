# reduce a no to 1 by performing given ops using min no of steps;
# divide by 2 if even
# either n-1 or n+1 if odd

def reduce1(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+reduce1(n//2)
    else:
        return min(1+reduce1(n+1),1+reduce1(n-1))
n=int(input("Enter a no: "))
t=reduce1(n)
print(t)

# ***use RECURSION when lots of possibilities are there***
# find all ways ,min or max ways etc uses recursion

# OR

# def reduce1(n,c):
#     if n==1:
#         return 0
#     elif n%2==0:
#         c=c+1
#         return 1+reduce1(n//2,c)
#     else:
#         c=c+1
#         return min(1+reduce1(n+1,c),1+reduce1(n-1,c))
# n=int(input("Enter a no: "))
# t=reduce1(n,0)
# print(t)

# this type of recursion is called tree recursion