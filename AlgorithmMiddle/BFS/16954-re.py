from collections import deque
MAP = []
visited = [[False for i in range(8)] for j in range(8)]
dir_x = [1, 0, -1, 0, 1, -1, 1, -1, 0]
dir_y = [0, 1, 0, -1, 1, -1, -1, 1, 0]

for i in range(8):
    MAP.append(list(input()))

def BFS():
    global visited
    Q = deque()
    Q.append([0, 7])
    visited[7][0] = True

    while Q:
        visited = [[False for i in range(8)] for j in range(8)]
        for _ in range(len(Q)):
            x, y = Q.popleft()
            if MAP[y][x] == '#':
                continue
            if x == 7 and y == 0:
                return 1
            for i in range(9):
                n_x = x + dir_x[i]
                n_y = y + dir_y[i]
                if 0 <= n_x < 8 and 0 <= n_y < 8:
                    if not visited[n_y][n_x] and MAP[n_y][n_x] != '#':
                        visited[n_y][n_x] = True
                        Q.append([n_x, n_y])
        
        MAP.pop()
        MAP.insert(0, ['0', '0', '0', '0', '0', '0', '0', '0'])
    
    return 0

res = BFS()
print(res)
