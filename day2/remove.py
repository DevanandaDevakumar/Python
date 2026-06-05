l1=[1,2,3,4,5,6,7]
print("rev:",l1[::-1])
# [7, 6, 5, 4, 3, 2, 1]
for i in l1:
    print("Removed",i)
    l1.remove(i)
print(l1)
# op:
# Removed 1
# Removed 3
# Removed 5
# Removed 7
# [2, 4, 6]
# Y?

# Soln:
l=[1,2,3,4,5,6,7]
n=len(l)
for i in range(n):
    print("Removed",l.pop(0))
print(l)
# op:
# Removed 1
# Removed 2
# Removed 3
# Removed 4
# Removed 5
# Removed 6
# Removed 7
# []