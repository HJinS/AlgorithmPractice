from collections import deque
from sys import maxsize
N = int(input())
board = []
visited = [[-1 for i in range(N)] for j in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
shark_size = 2
eat_cnt = 0
min_cnt, min_x, min_y = maxsize, maxsize, maxsize
res = 0

for i in range(N):
    board.append(list(map(int, input().split())))

shark = [(j, i) for i in range(N) for j in range(N) if board[i][j] == 9]
shark_x, shark_y = shark[0][0], shark[0][1]
board[shark_y][shark_x] = 0

def BFS(x, y):
    global min_cnt, min_x, min_y
    Q = deque()
    Q.append([x, y])
    visited[y][x] = 0

    while Q:
        cur_x, cur_y = Q.popleft()
        for i in range(4):
            n_x, n_y = cur_x + dir_x[i], cur_y + dir_y[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                if visited[n_y][n_x] != -1 or board[n_y][n_x] > shark_size:
                    continue
                visited[n_y][n_x] = visited[cur_y][cur_x] + 1
                if board[n_y][n_x] != 0 and board[n_y][n_x] < shark_size:
                    if min_cnt > visited[n_y][n_x]:
                        min_cnt = visited[n_y][n_x]
                        min_x = n_x
                        min_y = n_y
                    elif min_cnt == visited[n_y][n_x]:
                        if min_y == n_y:
                            if min_x > n_x:
                                min_x = n_x
                                min_y = n_y
                        elif min_y > n_y:
                            min_x = n_x
                            min_y = n_y
                Q.append([n_x, n_y])

while True:
    visited = [[-1 for i in range(N)] for j in range(N)]
    min_cnt, min_x, min_y = maxsize, maxsize, maxsize
    BFS(shark_x, shark_y)
    if min_x != maxsize and min_y != maxsize:
        res += visited[min_y][min_x]
        eat_cnt += 1
        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0
        board[min_y][min_x] = 0
        shark_x = min_x
        shark_y = min_y
    else:
        break
print(res)
