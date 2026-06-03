n=int(input("Enter a number:"))
l=len(str(n))
sum=0

while(n>0):
    for i in range(1,l+1):
        digit=n%10
        sum=sum+digit**i
        n=n//10
        print(sum)
print("Sum:",sum)

    
