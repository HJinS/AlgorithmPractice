from collections import deque
import sys

M, N = map(int, input().split())
box = []
Q = deque()
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 0

for i in range(N):
    box.append(list(map(int, input().split())))

for i in range(M):
    for j in range(N):
        if box[j][i] == 1:
            Q.append([i,j])

def bfs():

    while Q:
        loc = Q.popleft()
        x = loc[0]
        y = loc[1]
        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N and box[ny][nx] == 0:
                Q.append([nx,ny])
                box[ny][nx] = box[y][x] + 1

bfs()

for i in range(M):
    for j in range(N):
        if box[j][i] == 0:
            print("-1")
            sys.exit()
        else:
            res = max(res, box[j][i])

if res == 0:
    print("0")
else:
    print(res-1)
