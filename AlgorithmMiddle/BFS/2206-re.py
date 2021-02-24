from collections import deque
N, M = map(int, input().split())
board = []
visited = [[[-1 for i in range(2)] for j in range(M)] for k in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for i in range(N):
    board.append(list(map(int, input())))


def BFS():
    Q = deque()
    Q.append([0, 0, 0])
    visited[0][0][0] = 1

    while Q:
        x, y, z = Q.popleft()
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                if board[n_y][n_x] == 0:
                    if visited[n_y][n_x][z] == -1:
                        visited[n_y][n_x][z] = visited[y][x][z] + 1
                        Q.append([n_x, n_y, z])
                elif board[n_y][n_x] == 1:
                    if z == 0 and visited[n_y][n_x][1] == -1:
                        visited[n_y][n_x][1] = visited[y][x][z] + 1
                        Q.append([n_x, n_y, 1])
BFS()
res1, res2 = visited[N-1][M-1][0], visited[N-1][M-1][1]

if res1 == -1 and res2 != -1:
    print(res2)
elif res1 != -1 and res2 == -1:
    print(res1)
else:
    print(min(res1, res2))