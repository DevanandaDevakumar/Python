# reverse a list without rev 
# rev only 1st half
# 1 2 3 4 5 6 7 8
# op: 4 3 2 1 5 6 7 8

l=list(map(int,input().split()))
l1=l.copy()
print(l)
n=len(l)
j=-1
for i in range(n//2):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    j-=1
print(l)
j=n//2-1
for i in range(n//4):
    temp=l1[i]
    l1[i]=l1[j]
    l1[j]=temp
    j-=1
print(l1)