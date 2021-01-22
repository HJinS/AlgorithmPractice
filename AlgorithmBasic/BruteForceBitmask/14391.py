N, M = map(int, input().split())

arr = []
visited = [[False for i in range(M)] for j in range(N)]

res = 0

for i in range(N):
    arr.append(list(map(int, input())))

def arraySum():
    total = 0
    sum = 0
    for row in range(N):
        sum = 0
        for col in range(M):
            if visited[row][col] == True:
                sum = (sum * 10) + arr[row][col]
            else:
                total += sum
                sum = 0
        total += sum

    for col in range(M):
        sum = 0
        for row in range(N):
            if visited[row][col] == False:
                sum = (sum * 10) + arr[row][col]
            else:
                total += sum
                sum = 0
        total += sum
    return total


def solve(y, x):
    global res
    if y == N:
        res = max(res, arraySum())
        return
    if x == M:
        solve(y+1, 0)
        return
    visited[y][x] = True
    solve(y, x+1)
    visited[y][x] = False
    solve(y, x+1)

solve(0,0)
print(res)