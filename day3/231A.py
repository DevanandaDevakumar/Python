n=int(input())
s=0
for i in range(n):
    c=0
    c=sum(map(int,input().split()))
    if c>1:
        s+=1
print(s)