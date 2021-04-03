N, K = map(int, input().split())

calK = K
num_cnt = 9
total_num = 0
num_length = 1
tenten = 1
res = 0

while calK > num_cnt * num_length:
    total_num += num_cnt
    calK -= num_cnt  * num_length
    num_cnt *= 10
    num_length += 1

total_num += (calK-1) // num_length + 1

if total_num > N:
    res = -1
    print(res)
else:
    tmp = (calK - 1) % num_length + 1
    for i in range(num_length-1):
        tenten *= 10
    
    for i in range(tmp):
        res = total_num // tenten
        total_num %= tenten
        tenten //= 10

    print(res)