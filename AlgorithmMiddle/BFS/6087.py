from collections import deque
from sys import maxsize
W, H = map(int, input().split())
board = []
visited = [[maxsize for i in range(W)] for j in range(H)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
for i in range(H):
    board.append(list(input()))
start_x, start_y = -1, -1
res = maxsize

def BFS(start_x, start_y):
    global res, end_x, end_y
    Q = deque()
    Q.append([start_x, start_y])
    visited[start_y][start_x] = 0

    while Q:
        x, y = Q.popleft()
        if x == end_x and y == end_y:
            res = min(res, visited[y][x]-1)
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            while True:
                if 0 <= n_x < W and 0 <= n_y < H:
                    if visited[n_y][n_x] != -1 and visited[n_y][n_x] < visited[y][x] + 1:
                        break
                    if board[n_y][n_x] == '*':
                        break
                    Q.append([n_x, n_y])
                    visited[n_y][n_x] = visited[y][x] + 1
                    n_y = n_y + dir_y[i]
                    n_x = n_x + dir_x[i]
                else:
                    break
tmp = []
for i in range(H):
    for j in range(W):
        if board[i][j] == "C":
            tmp.append([j, i])
[start_x, start_y], [end_x, end_y] = tmp

BFS(start_x, start_y)
print(res)