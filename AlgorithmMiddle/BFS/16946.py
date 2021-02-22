from collections import deque
N, M = map(int, input().split())
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
board = []
board_num = [[0 for i in range(M)] for j in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
v = {}

for i in range(N):
    board.append(list(map(int, input())))

def BFS(start_x, start_y, num):
    Q = deque()
    Q.append([start_x, start_y])
    visited[start_y][start_x] = True
    cnt = 1

    while Q:
        x, y = Q.popleft()
        board_num[y][x] = num

        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]

            if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                if board[n_y][n_x] == 0:
                    if not visited[n_y][n_x]:
                        visited[n_y][n_x] = True
                        Q.append([n_x, n_y])
                        cnt += 1
    return cnt

def numbering():
    num = 1
    for i in range(N):
        for j in range(M):
            if not board[i][j] and not visited[i][j]:
                v[num] = BFS(j, i, num)
                num += 1

def solve():
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                s = set()
                for k in range(4):
                    n_x = j + dir_x[k]
                    n_y = i + dir_y[k]
                    if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                        if board_num[n_y][n_x] != 0:
                            s.add(board_num[n_y][n_x])
                for k in s:
                    board[i][j] += v[k]
                    board[i][j] %= 10

numbering()
solve()

for i in range(N):
    for j in range(M):  
        print(board[i][j], end='')
    print()

