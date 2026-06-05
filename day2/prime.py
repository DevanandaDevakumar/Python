# n=int(input("Enter a number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if(count==2):
#     print("Prime")
# else:
#     print("Not prime")



# n=int(input("Enter a number"))
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
# if(flag==0):
#     print("Prime")
# else:
#     print("Not prime")



n=int(input("Enter a number"))
flag=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        flag=1
        break
if(flag==0):
    print("Prime")
else:
    print("Not prime")