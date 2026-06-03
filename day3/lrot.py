#rotate left by 1 position
l=[1,2,3,4,5,6,7]
a=l[0]
print(l)
for i in range(len(l)-1):
    l[i]=l[i+1]
l[-1]=a
print(l)

print()
#rot left by 2 pos 
l=[1,2,3,4,5,6,7]
a=l[0]
b=l[1]
print(l)
for i in range(len(l)-2):
    l[i]=l[i+2]
l[-1]=b
l[-2]=a
print(l)

# print()
# #rot left by k pos 
# l=[1,2,3,4,5,6,7]
# k=int(input())%len(l)
# a=[]
# print(l)
# for i in range(len(l)-2):
#     l[i]=l[i+2]
# l[-1]=b
# l[-2]=a
# print(l)

print()
#rotate right by 1 position
l=[1,2,3,4,5,6,7]
a=l[-1]
print(l)
for i in range(len(l)-1,0,-1):
    l[i]=l[i-1]
l[0]=a
print(l)

print()
#rotate right by 2 position
l=[1,2,3,4,5,6,7]
a=l[-1]
b=l[-2]
print(l)
for i in range(len(l)-1,0,-1):
    l[i]=l[i-2]
l[0]=b
l[1]=a
print(l)