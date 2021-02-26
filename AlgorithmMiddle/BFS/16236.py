from collections import deque
import sys
N = int(input())
board = []
dir_x = [0, -1, 0, 1]
dir_y = [-1, 0, 1, 0]
shark_size = 2
dis = [[-1 for i in range(N)] for j in range(N)]
min_dis, min_x, min_y = sys.maxsize, sys.maxsize, sys.maxsize
eat_cnt = 0
res = 0

for i in range(N):
    board.append(list(map(int, input().split())))

shark = [(j, i) for i in range(N) for j in range(N) if board[i][j] == 9]
shark_x, shark_y = shark[0][0], shark[0][1]
board[shark_y][shark_x] = 0

def BFS(x, y):
    global min_dis, min_x, min_y
    Q = deque()
    Q.append([x, y])
    dis[y][x] = 0
    cnt = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                if dis[n_y][n_x] != -1 or board[n_y][n_x] > shark_size:
                    continue
                dis[n_y][n_x] = dis[y][x] + 1
                if board[n_y][n_x] != 0 and board[n_y][n_x] < shark_size:
                    if min_dis > dis[n_y][n_x]:
                        min_x = n_x
                        min_y = n_y
                        min_dis = dis[n_y][n_x]
                    elif min_dis == dis[n_y][n_x]:
                        if min_y == n_y:
                            if min_x > n_x:
                                min_x = n_x
                                min_y = n_y
                        elif min_y > n_y:
                            min_x = n_x
                            min_y = n_y
                Q.append([n_x, n_y])

while True:
    dis = [[-1 for i in range(N)] for j in range(N)]
    min_dis, min_x, min_y = sys.maxsize, sys.maxsize, sys.maxsize
    BFS(shark_x, shark_y)
    if min_x != sys.maxsize and min_y != sys.maxsize:
        res += dis[min_y][min_x]
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