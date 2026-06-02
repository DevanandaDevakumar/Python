n=int(input())
n1=n
s=0
while(n1>0):
    if(n1>=5):
        s+=n1//5
        n1=(n1%5)
    elif n1>=4:
        s+=n1//4
        n1=(n1%4)
    elif n1>=3:
        s+=n1//3
        n1=(n1%3)
    elif n1>=2:
        s+=n1//2
        n1=n1%2
    elif n1>=1:
        s+=n1
        n1=n1-n1
print(s)