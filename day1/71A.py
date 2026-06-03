#https://codeforces.com/problemset/problem/71/A
n=int(input())
for i in range(n):
    s=input()
    l=len(s)
    if l>10:
        s1=s[0]+str(l-2)+s[l-1]
    else:
        s1=s
    print(s1)