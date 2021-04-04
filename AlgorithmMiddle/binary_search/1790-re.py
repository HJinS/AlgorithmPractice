N, K = map(int, input().split())

cal_K = K
skip_num = 9
len_num = 1
total_num = 0
res = 0

while cal_K > skip_num * len_num:
    total_num += skip_num
    cal_K -= skip_num * len_num
    skip_num *= 10
    len_num += 1

total_num += (cal_K - 1) // len_num + 1
if total_num > N:
    res = -1
else:
    tmp = (cal_K - 1) % len_num + 1
    divided_num = int(10 ** (len_num - 1))
    for i in range(tmp):
        res = total_num // divided_num
        total_num %= divided_num
        divided_num //= 10
print(res)