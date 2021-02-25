from collections import deque
chess = []
dir_x = [1, 0, -1, 0, 1, -1, 1, -1, 0]
dir_y = [0, 1, 0, -1, 1, -1, -1, 1, 0]

for i in range(8):
    chess.append(list(input()))

def BFS():
    Q = deque()
    Q.append([0, 7])

    while Q:
        visited = [[False]*8 for i in range(8)]
        for _ in range(len(Q)):
            x, y = Q.popleft()
            if x == 7 and y == 0:
                return 1
            if chess[y][x] == '#':
                continue
            for i in range(9):
                n_x = x + dir_x[i]
                n_y = y + dir_y[i]

                if 0 <= n_x < 8 and 0 <= n_y < 8:
                    if chess[n_y][n_x] == '.':
                        if not visited[n_y][n_x]:
                            visited[n_y][n_x] = True
                            Q.append([n_x, n_y])
        chess.pop()
        chess.insert(0,['.', '.', '.', '.', '.', '.', '.', '.'])
    return 0

res = BFS()
print(res)
