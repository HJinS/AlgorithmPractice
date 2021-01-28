from collections import deque
import sys
T = int(sys.stdin.readline())

state = [[]]
visited = [[]]

dir_x = [2,2,1,1,-1,-1,-2,-2]
dir_y = [1,-1,2,-2,2,-2,1,-1]

def bfs(x, y, des_x, des_y, length):
    Q = deque()
    Q.append([x,y])
    visited[y][x] = 1
    state[y][x] = 0
    while Q:
        now = Q.popleft()
        now_x = now[0]
        now_y = now[1]
        if now_x == des_x and now_y == des_y:
            return
        for i in range(8):
            nx = now_x + dir_x[i]
            ny = now_y + dir_y[i]
            if nx >= 0 and nx < length and ny >= 0 and ny < length and visited[ny][nx] == 0:
                state[ny][nx] = min(state[ny][nx], state[now_y][now_x] + 1)
                visited[ny][nx] = 1
                Q.append([nx,ny])

for _ in range(T):
    length = int(sys.stdin.readline())
    now_y, now_x = map(int, sys.stdin.readline().split())
    des_y, des_x = map(int, sys.stdin.readline().split())
    state = [[9876543 for i in range(length)] for j in range(length)]
    visited = [[0 for i in range(length)] for j in range(length)]
    bfs(now_x, now_y, des_x, des_y, length)
    print(state[des_y][des_x])