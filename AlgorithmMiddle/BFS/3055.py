from collections import deque
R, C = map(int, input().split())
forest = []
water = {}
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
water_cnt = 0
visited = [[False for i in range(C)] for j in range(R)]

for i in range(R):
    forest.append(list(input()))

def spreadWater():
    global water_cnt
    tmp = water_cnt
    for j in range(tmp):
        w = water[j]
        x, y = w[0], w[1]
        for i in range(4):
            n_x, n_y = x + dir_x[i], y + dir_y[i]
            if n_x >= 0 and n_x < C and n_y >= 0 and n_y < R:
                if forest[n_y][n_x] == '.':
                    forest[n_y][n_x] = '*'
                    water[water_cnt] = [n_x, n_y]
                    water_cnt += 1

def BFS():
    global water_cnt
    Q = deque()
    for i in range(R):
        for j in range(C):
            if forest[i][j] == 'S':
                Q.append([j, i, 0])
            elif forest[i][j] == '*':
                water[water_cnt] = [j, i]
                water_cnt += 1
    
    while Q:
        for _ in range(len(Q)):
            x, y, cnt = Q.popleft()
            if forest[y][x] == 'D':
                return cnt
            if forest[y][x] == '*':
                continue
            for i in range(4):
                n_x, n_y = x + dir_x[i], y + dir_y[i]
                if 0 <= n_x < C and 0 <= n_y < R:
                    if (forest[n_y][n_x] == '.' or forest[n_y][n_x] == 'D') and not visited[n_y][n_x]:
                        visited[n_y][n_x] = True
                        Q.append([n_x, n_y, cnt+1])
        spreadWater()
    return -1

res = BFS()
if res == -1:
    print("KAKTUS")
else:
    print(res)