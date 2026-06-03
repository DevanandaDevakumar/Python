# arr = []
# num = 1
# while len(arr) < 1000:
#     if num % 3 != 0 and num % 10 != 3:
#         arr.append(num)
#     num += 1
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     print(arr[k - 1])

t=int(input())
for _ in range(t):
    k=int(input())
    cnt=0
    num=1
    while cnt<k:
        if num%3!=0 and num%10!=3:
            cnt+=1
        num+=1
    print(num-1)