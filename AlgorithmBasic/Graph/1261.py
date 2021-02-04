from queue import PriorityQueue

M, N = map(int, input().split())
maze = [[] for i in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 987654312
visited = [[False for i in range(M)] for j in range(N)]

for i in range(N):
    maze[i] = list(map(int, input()))

def BFS(x, y, cnt):
    Q = PriorityQueue()
    Q.put([cnt, x, y])

    while Q.empty() == False:
        e = Q.get()
        cnt = e[0]
        x = e[1]
        y = e[2]

        if x == M-1 and y == N-1:
            return cnt

        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]

            if nx >=0 and nx < M and ny >= 0 and ny < N and not visited[ny][nx]:
                if maze[ny][nx] == 1:
                    Q.put([cnt + 1, nx, ny])
                else:
                    Q.put([cnt, nx, ny])
                visited[ny][nx] = True

res = BFS(0, 0, 0)
print(res)