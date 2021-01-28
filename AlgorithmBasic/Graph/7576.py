import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []

res = 0
state = [0 for i in range(M * N)]
Q = deque()
dir_x = [1,0,-1,0]
dir_y = [0,1,0,-1]

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append([j,i])

def bfs():
    global Q
    while Q:
        v = Q.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = v[0] + dir_x[i]
            ny = v[1] + dir_y[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                Q.append([nx, ny])

bfs()

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print("-1")
            sys.exit()
        else:
            res = max(res, box[i][j])

if res == 1:
    print("0")
else:
    print(res-1)

'''
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []

ver = [i for i in range(M * N)]
edge = [[] for i in range(M * N)]
visited = [-1 for i in range(M * N)]
res = 0
state = [0 for i in range(M * N)]
Q = deque()

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == -1:
            continue
        if i > 0 and box[i-1][j] != -1:
            edge[i*M+j].append((i-1)*M+j)
        if i < N-1 and box[i+1][j] != -1:
            edge[i*M+j].append((i+1)*M+j)
        if j > 0 and box[i][j-1] != -1:
            edge[i*M+j].append(i*M+(j-1))
        if j < M-1 and box[i][j+1] != -1:
            edge[i*M+j].append(i*M+(j+1))
        visited[i*M+j] = box[i][j]
        if box[i][j] == 1:
            Q.append(i*M+j)

def bfs():
    global Q
    while Q:
        e = Q.popleft()
        for i in range(len(edge[e])):
            adj_v = edge[e][i]
            if visited[adj_v] == 0:
                Q.append(adj_v)
                visited[adj_v] = 1
                state[adj_v] = state[e] + 1

bfs()

for i in range(N*M):
    if visited[i] == 0:
        print("-1")
        sys.exit()
    elif visited[i] == 1:
        res = max(res, state[i])

if res == 1:
    print("0")
else:
    print(res)
'''
