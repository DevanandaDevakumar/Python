#segregate the given list as an even elements 1st in descending order and then odd elements next in ascending order
l=list(map(int,input().split())) # 6 2 1 4 3 7 5
l.sort() # 1 2 3 4 5 6 7
res=[]
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)
#op:
# 6 2 1 4 3 7 5
# [6, 4, 2, 1, 3, 5, 7]