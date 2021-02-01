from collections import deque
import sys

sys.setrecursionlimit(100000)

N = int(input())
world_map = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
visited = [[False for i in range(N)] for j in range(N)]
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

    Q = deque()
    for i in range(N):
        for j in range(N):
            if world_map[j][i] == cnt:
                visited[j][i] = True
                Q.append([i,j])
    dis = 0
    while Q:
        for i in range(len(Q)):
            e = Q.popleft()
            now_x = e[0]
            now_y = e[1]
            for i in range(4):
                new_x = now_x + dir_x[i]
                new_y = now_y + dir_y[i]

                if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                    if world_map[new_y][new_x] and world_map[new_y][new_x] != cnt:
                        return dis
                    elif not world_map[new_y][new_x] and not visited[new_y][new_x]:
                        Q.append([new_x, new_y])
                        visited[new_y][new_x] = True
        dis += 1

cnt = 1
for i in range(N):
    for j in range(N):
        if not visited[j][i] and world_map[j][i]:
            dfs(i,j,cnt)
            cnt += 1

for i in range(1, cnt):
    visited = [[False for i in range(N)] for j in range(N)]
    tmp = bfs(i)
    res = min(res, tmp)

print(res)
                    