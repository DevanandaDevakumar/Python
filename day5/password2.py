print("Enter a password with atleast one uppercase letter, one Lowercase letter, digits(0-9), special character(@,_) \nand has atleast 8 characters: ",end="")
s=input()
l=len(s)
if l<8:
    print("Invalid: Does not contain atleast 8 character")
    exit()
u=False
l=False
d=False
special=False
space=False
for i in s:
    if i.isupper():
        u=True
    elif i.islower():
        l=True
    elif i.isdigit():
        d=True
    elif i.isspace():
        space=True
        break
    else:
        special=True
if not space and special and l and d and u:
    print("Valid")
else:
    print("Invalid")