from collections import deque
import copy
N, M = map(int, input().split())
MAP = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 0

for i in range(N):
    MAP.append(list(map(int, input().split())))

def BFS():
    global res, MAP
    Q = deque()
    copy_map = copy.deepcopy(MAP)
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] == 2:
                Q.append([j, i])

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                if copy_map[n_y][n_x] == 0:
                    copy_map[n_y][n_x] = 2
                    Q.append([n_x, n_y])

    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] == 0:
                cnt += 1
    res = max(res, cnt)

def solve(cnt):
    if cnt == 3:
        BFS()
        return

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                solve(cnt + 1)
                MAP[i][j] = 0

solve(0)
print(res)