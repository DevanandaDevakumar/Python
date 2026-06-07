# chars = ["a","a","a","a","a","b","b","b","b","b","c","c","c","a","a"]
# s = ""
# i = 0
# n = len(chars)
# while i < n:
#     j = i
#     while j < n and chars[j] == chars[i]:
#         j += 1
#     cnt = j - i
#     s += chars[i]
#     if cnt > 1:
#         s += str(cnt)
#     i = j
# print(s)

chars = ["a","a","a","a","a","b","b","b","b","b","c","c","c","a","a"]
res = ""
c,k=1,0
for i in range(1,len(chars)):
    if chars[k]==chars[i]:
        c=c+1
    else:
        res=res+chars[i-1]+str(c)
        k=i
        c=1
res=res+chars[-1]+str(c)
print(res)