l=[1,3,5,6,7,8,10,12,13,15]
def binary(l,h,m,k):
    while l<h:
        if k==l[m]:
            return True
        elif k>l[m]:
            return binary(m+1,h,(h+l)//2,k)
        else:
            return binary(l,m-1,(h+l)//2,k)
    else:
        return False
k=int(input())
print(binary(0,len(l)-1,((len(l)-1)//2),k))