n=int(input("Enter a number:"))
temp=n
l=len(str(n))
num=0
while(n>0):
    digit=n%10
    num=num+digit**l
    n=n//10
if(temp==num):
    print("Armstrong number")
else:
    print("Not armstrong")
