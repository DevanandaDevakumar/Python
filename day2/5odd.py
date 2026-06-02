#print the elements in the list with odd no. of occurence
l=list(map(int,input().split()))
l2=[]
for i in l:
    if l.count(i)%2!=0 and i not in l2:
        l2.append(i)
print(l2)