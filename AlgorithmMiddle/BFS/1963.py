from collections import deque
T = int(input())
Is_Prime = [True for i in range(10000)]
visited = [False for i in range(10000)]

for i in range(2, int(10000 ** 0.5) + 1):
    if Is_Prime[i]:
        for j in range(i*2, 10000, i):
            Is_Prime[j] = False

def replace(num, digit, loc):
    tmp = num
    for i in range(loc):
        tmp = int(tmp) / 10
    quo = int(tmp) % 10
    res = num - int(quo * (10 ** loc))
    res += int(digit * (10 ** loc))
    return int(res)

def BFS(start_num, des_num):
    Q = deque()
    Q.append([start_num, 0])
    visited[start_num] = True
    while Q:
        num, cnt = Q.popleft()
        if num == des_num:
            return cnt
        for i  in range(4):
            for j in range(10):
                new_num = replace(num, j, i)
                if new_num >= 1000 and new_num < 10000 and not visited[new_num] and Is_Prime[new_num]:
                    visited[new_num] = True
                    Q.append([new_num, cnt + 1])
    return -1

for i in range(T):
    start, des = map(int, input().split())
    visited = [False for i in range(10000)]
    res = BFS(start, des)
    if res == -1:
        print("Impossible")
    else:
        print(res)