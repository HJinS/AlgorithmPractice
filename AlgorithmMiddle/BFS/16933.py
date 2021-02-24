from collections import deque
N, M, K = map(int, input().split())
MAP = []
visited = [[[False for i in range(K+1)] for j in range(M)] for k in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for i in range(N):
    MAP.append(list(map(int, input())))

def BFS():
    Q = deque()
    Q.append([0, 0, 0, 1])
    visited[0][0][0] = 1
    day = True
    while Q:
       
        for _ in range(len(Q)):
            x, y, break_cnt, dis = Q.popleft()
            if x == M-1 and y == N-1:
                return dis
            for i in range(4):
                n_x = x + dir_x[i]
                n_y = y + dir_y[i]
                if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                    if MAP[n_y][n_x] == 0:
                        if not visited[n_y][n_x][break_cnt]:
                            visited[n_y][n_x][break_cnt] = True
                            Q.append([n_x, n_y, break_cnt, dis+1])
                    elif MAP[n_y][n_x] == 1:
                        if break_cnt >= 0 and break_cnt < K:
                            if day:
                                if not visited[n_y][n_x][break_cnt+1]:
                                    visited[n_y][n_x][break_cnt+1] = True
                                    Q.append([n_x, n_y, break_cnt+1, dis+1])
                            else:
                                if not visited[n_y][n_x][break_cnt+1]:
                                    Q.append([x, y, break_cnt, dis+1])
        day = not day
    return -1

res = BFS()

print(res)