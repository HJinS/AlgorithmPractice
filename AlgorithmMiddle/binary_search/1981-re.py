from collections import deque
N = int(input())
arr = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for i in range(N):
    arr.append(list(map(int, input().split())))

def BFS(min_n, max_n):
    Q = deque()
    visited = [[False for i in range(N)] for j in range(N)]
    if arr[0][0] < min_n or arr[0][0] > max_n:
        return False
    Q.append([0, 0])
    visited[0][0] = True

    while Q:
        x, y = Q.popleft()
        if x == N-1 and y == N-1:
            return True
        for i in range(4):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                if not visited[n_y][n_x] and min_n <= arr[n_y][n_x] <= max_n:
                    visited[n_y][n_x] = True
                    Q.append([n_x, n_y])
    return False

def check(mid):
    idx = 0
    while idx + mid <= 200:
        res = BFS(idx, idx+mid)
        idx += 1
        if res:
            return True
    return False


l, r = 0, max(map(max, arr))
res = 987654321
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        res = min(res, mid)
        r = mid - 1
    else:
        l = mid + 1

print(res)