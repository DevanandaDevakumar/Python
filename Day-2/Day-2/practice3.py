# print the elements in the list which has occured odd number of times

n=list(input().split())
new=[]
for i in n:
    if i not in new and n.count(i)%2!=0:
        new.append(i)
print(new)