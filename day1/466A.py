n,m,a,b=map(int,input().split())
if(a*m<b):
    print(a*n)
else:
    s=(n//m*b)+ min(n%m*a,b)
    print(s)