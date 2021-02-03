from collections import deque
import sys

sys.setrecursionlimit(100000)

N = int(input())
world_map = []
visited = [[False for i in range(N)] for j in range(N)]
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]
res = 987654321

for i in range(N):
    world_map.append(list(map(int, input().split())))

def dfs(x, y, cnt):
    visited[y][x] = True
    world_map[y][x] = cnt
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and not visited[ny][nx]:
            if world_map[ny][nx]:
                dfs(nx, ny, cnt)


def bfs(cnt):
    visited = [[False for i in range(N)] for j in range(N)]
    Q = deque()

    for i in range(N):
        for j in range(N):
            if world_map[j][i] == cnt:
                Q.append([i, j])
                visited[j][i] = True
    dis = 0
    while Q:
        for i in range(len(Q)):
            e = Q.popleft()
            x = e[0]
            y = e[1]
            for i in range(4):
                nx = x + dir_x[i]
                ny = y + dir_y[i]
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    if world_map[ny][nx] and world_map[ny][nx] != cnt:
                        return dis
                    elif not visited[ny][nx] and not world_map[ny][nx]:
                        Q.append([nx, ny])
                        visited[ny][nx] = True
        dis += 1

                        
cnt = 1
for i in range(N):
    for j in range(N):
        if not visited[j][i] and world_map[j][i] == 1:
            dfs(i, j, cnt)
            cnt += 1


for i in range(1, cnt):
    tmp = bfs(i)
    res = min(res, tmp)

print(res)