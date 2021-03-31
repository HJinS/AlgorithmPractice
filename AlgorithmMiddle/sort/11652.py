n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

cnt = 0
tmp = arr[0]
res = 0
ans = 0
for i in range(n):
    if tmp == arr[i]:
        cnt += 1
    else:
        if res < cnt:
            res = cnt
            ans = tmp
        tmp = arr[i]
        cnt = 1
if res < cnt:
    res = cnt
    ans = tmp
print(ans)