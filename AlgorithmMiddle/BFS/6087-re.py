from collections import deque
from sys import maxsize
W, H = map(int, input().split())
board = []
visited = [[-1 for i in range(W)] for j in range(H)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = maxsize

for i in range(H):
    board.append(list(input()))

loc = []
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            loc.append([j, i])

start = loc[0]
end = loc[1]

def BFS():
    global res
    Q = deque()
    Q.append([start[0], start[1]])
    visited[start[1]][start[0]] = 0

    while Q:
        x, y = Q.popleft()
        if x == end[0] and y == end[1]:
            res = min(res, visited[y][x]-1)
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            while True:
                if not (0 <= n_x < W and 0 <= n_y < H):
                    break
                if board[n_y][n_x] == "*":
                    break
                if visited[n_y][n_x] != -1 and visited[n_y][n_x] < visited[y][x] + 1:
                    break
                visited[n_y][n_x] = visited[y][x] + 1
                Q.append([n_x, n_y])
                n_x += dir_x[i]
                n_y += dir_y[i]

BFS()
print(res)