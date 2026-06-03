l1=[1,2,3,4,5,6,7]
print(l1[::-1])
for i in l1:
    print("Removed",i)
    l1.remove(i)
print(l1)

