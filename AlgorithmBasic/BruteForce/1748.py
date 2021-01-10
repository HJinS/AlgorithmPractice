n = int(input())
res = 0
for i in range(1,n+1):
    cnt = 0
    n = i
    while n > 0:
        cnt += 1
        n = n // 10
    res += cnt
print(res)