from collections import deque
N = int(input())

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 987654321
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))


def BFS(min_n, max_n):
    visited = [[False for i in range(N)] for j in range(N)]
    if arr[0][0] < min_n or arr[0][0] > max_n:
        return False
    Q = deque()
    Q.append([0, 0])
    visited[0][0] = True

    while Q:
        x, y = Q.popleft()
        if x == N-1 and y == N-1:
            return True
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if n_x >= 0 and n_x < N and n_y >= 0 and n_y < N:
                if visited[n_y][n_x] == False and min_n <= arr[n_y][n_x] <= max_n:
                    visited[n_y][n_x] += 1
                    Q.append([n_x, n_y])
    return False

def check(diff):
    i = 0
    while i+diff <= 200:
        if BFS(i, i+mid):
            return True
        i += 1
    return False

l, r = 0, max(map(max, arr))
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        res = min(res, mid)
        r = mid - 1
    else:
        l = mid + 1
print(res)