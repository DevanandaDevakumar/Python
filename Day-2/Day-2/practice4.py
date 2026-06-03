# segregate the given list as even numbers first in descending order and then odd elements next in ascending order
n=list(map(int,input().split()))
n.sort()
res=[]
for i in n:
    # add even number at last
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)