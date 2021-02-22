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
    global res
    Q = deque()
    tmp_MAP = copy.deepcopy(MAP)
    visited = [[False for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if tmp_MAP[i][j] == 2:
                Q.append([j, i])
                visited[i][j] = True
    
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                if tmp_MAP[ny][nx] == 0:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        Q.append([nx, ny])
                        tmp_MAP[ny][nx] = 2
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_MAP[i][j] == 0:
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