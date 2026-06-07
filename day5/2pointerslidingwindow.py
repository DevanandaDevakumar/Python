# find max length in array such that the sum of elements in that subarray is <=k
# dynamic sliding window
list=[2,1,6,2,1,2,4,7,8,1,2]
k=10
r,l,s,m=0,0,0,0
while r<len(list):
    s=s+list[r]
    while s>k:
        s=s-list[l]
        l=l+1
    length=r-l+1
    m=max(length,m)
    r=r+1
print(m)