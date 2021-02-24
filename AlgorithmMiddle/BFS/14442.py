from collections import deque
N, M, K = map(int, input().split())
MAP = []
visited = [[[-1 for i in range(K+1)] for j in range(M)] for k in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for i in range(N):
    MAP.append(list(map(int, input())))

def BFS():
    Q = deque()
    Q.append([0, 0, 0])
    visited[0][0][0] = 1

    while Q:
        x, y, break_cnt = Q.popleft()
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                if MAP[n_y][n_x] == 0 and visited[n_y][n_x][break_cnt] == -1:
                    visited[n_y][n_x][break_cnt] = visited[y][x][break_cnt] + 1 
                    Q.append([n_x, n_y, break_cnt])
                elif MAP[n_y][n_x] == 1:
                    if break_cnt >= 0 and break_cnt < K:
                        if visited[n_y][n_x][break_cnt+1] == -1:
                            visited[n_y][n_x][break_cnt+1] = visited[y][x][break_cnt] + 1
                            Q.append([n_x,n_y,break_cnt+1])

BFS()

res = 98765321
for v in visited[N-1][M-1]:
    if v != -1:
        res = min(res, v)

if res == 98765321:
    res = -1
print(res)