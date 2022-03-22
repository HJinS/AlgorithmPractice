from collections import deque
N = int(input())
power = list(map(int, input().split(' ')))

des_cnt = 0
des_Q = deque()
for i in range(1, len(power)):
    if power[i] < power[i-1]:
        des_cnt += 1
    else:
        des_Q.append([des_cnt, i])
        des_cnt = 0

des_list = list(des_Q)
des_list.sort(key = lambda x:-x[0])
des_Q = deque(des_list)
cur_idx = 0
cnt = 0
while des_Q:
    des_cnt, idx = des_Q.popleft()
    if cur_idx < idx:
        cur_idx = idx
        cnt += 1
    else:
        cur_idx += 1

print(cnt)
