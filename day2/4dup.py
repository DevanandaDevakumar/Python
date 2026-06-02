#print the list after deleting the duplicate elements in it
#ip:read a list op: print list after deleting duplicate elements
a=list(input().split())
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
# print(*b) without list like appearence

# op:hello 1 2 3 2 4 1 5 10 21 10 1
# ['hello', '1', '2', '3', '4', '5', '10', '21']
