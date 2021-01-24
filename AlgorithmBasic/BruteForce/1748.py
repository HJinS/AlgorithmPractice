n = int(input())
res = 0
n_cnt = 0
for i in range(1,n+1):
    if i >= 10 ** n_cnt and i < 10 ** (n_cnt+1):
        res += n_cnt + 1
        if i == 10 ** (n_cnt+1) - 1:
            n_cnt += 1
print(res)