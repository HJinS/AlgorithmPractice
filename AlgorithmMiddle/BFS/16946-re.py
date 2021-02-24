from collections import deque
N, M = map(int, input().split())
MAP = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
visited = [[False for i in range(M)] for j in range(N)]
num_MAP = [[0 for i in range(M)] for j in range(N)]
v = {}

for i in range(N):
    MAP.append(list(map(int, input())))

def BFS(start_x, start_y, num):
    Q = deque()
    Q.append([start_x, start_y])
    visited[start_y][start_x] = True
    cnt = 1
    while Q:
        x, y = Q.popleft()
        num_MAP[y][x] = num
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                if MAP[n_y][n_x] == 0 and not visited[n_y][n_x]:
                    visited[n_y][n_x] = True
                    Q.append([n_x, n_y])
                    cnt += 1
    return cnt

def numbering():
    num = 1
    for i in range(N):
        for j in range(M):
            if not MAP[i][j]:
                if not visited[i][j]:
                    res = BFS(j, i, num)
                    v[num] = res
                    num += 1

def solve():
    for i in range(N):
        for j in range(M):
            if MAP[i][j]:
                s = set()
                for k in range(4):
                    n_x = j + dir_x[k]
                    n_y = i + dir_y[k]
                    if n_x >= 0 and n_x < M and n_y >= 0 and n_y < N:
                        if num_MAP[n_y][n_x] != 0:
                            s.add(num_MAP[n_y][n_x])
                for k in s:
                    MAP[i][j] += v[k]
                    MAP[i][j] %= 10
numbering()
solve()

for i in range(N):
    for j in range(M):
        print(MAP[i][j], end='')
    print()
