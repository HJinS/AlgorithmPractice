from queue import PriorityQueue

M, N = map(int, input().split())
maze = [[] for i in range(N)]
visited = [[False for i in range(M)] for i in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 0
for i in range(N):
    maze[i] = list(map(int, input()))

def BFS(x, y):
    Q = PriorityQueue()
    Q.put([0, x, y])
    visited[y][x] = True

    while not Q.empty():
        e = Q.get()
        cnt = e[0]
        now_x = e[1]
        now_y = e[2]

        if now_x == M-1 and now_y == N-1:
            return cnt

        for i in range(4):
            new_x = now_x + dir_x[i]
            new_y = now_y + dir_y[i]

            if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N and not visited[new_y][new_x]:
                if maze[new_y][new_x] == 1:
                    Q.put([cnt + 1, new_x, new_y])
                else:
                    Q.put([cnt, new_x, new_y])
                visited[new_y][new_x] = True

res = BFS(0, 0)
print(res)