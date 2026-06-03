#print a list after deleting duplicate elements from it
# n=list(map(int,input().split()))
n=list(input().split())
new=[]
for i in n:
    if i not in new:
        new.append(i)
print(new)