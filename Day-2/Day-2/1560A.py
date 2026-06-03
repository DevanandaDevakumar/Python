t=int(input())
for i in range(t):
    n=int(input())
    i=1
    k=0
    while 1:
        # not divisible by 3 and not ending by 3
        if i%3!=0 and i%10!=3:
            if n==k:
                print(i)
                break
            k=k+1
        i=i+1