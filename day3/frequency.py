# l=[1,3,1,3,1,2,1,4,2,2,2,2,2]
# max=0
# for i in l:
#     if l.count(i)>max:
#         max=i
# print(max)

l=[1,3,1,3,1,2,1,4,2,2,2,2,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ele1=0
freq1=0
ele2=0
freq2=0
for i in d:
    if d[i]>freq1:
        freq2=freq1
        ele2=ele1
        freq1=d[i]
        ele1=i
    if d[i]>freq2 and d[i]!=freq1:
        freq2=d[i]
        ele2=i
print("max element is ",ele1,"with occurence ",freq1,"\n2nd max element is ",ele2,"with occurence ",freq2)
