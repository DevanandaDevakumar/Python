print("Enter a password with atleast one uppercase letter, one Lowercase letter, digits(0-9), special character(@,_) \nand has atleast 8 characters: ",end="")
s=input()
l=len(s)
if l<8:
    print("invalid")
    exit()
u=0
l=0
d=0
sp=0
for i in s:
    if i.isalpha():
        if i.isupper():
            u=u+1
        else:
            l=l+1
    elif i.isdigit():
        d=d+1
    elif i in ['@','_']:
        sp=sp+1
    elif i.isspace():
        print("invalid")
        break
    else:
        print("invalid")
        break
if sp>0 and u>0 and l>0 and d>0:
    print("Valid")
else:
    print("Invalid")