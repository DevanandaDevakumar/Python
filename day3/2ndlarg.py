l=[5,4,3,2]
b=0
sb=0
for i in l:
    if i>b:
        sb=b
        b=i
    elif sb<i and i!=b:
        sb=i
print("Largest: ",b,"\nSecond Largest: ",sb)