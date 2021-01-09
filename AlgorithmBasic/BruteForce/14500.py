n, m = map(int, input().split())

page = []
visited = [[False for i in range(500)] for j in range(500)]
dir = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    page.append(list(map(int, input().split())))


def DFS(y, x, cnt):
    if cnt == 4:
        return page[y][x]
    sum = 0

    for i in range(4):
        nextY = y + dir[i][0]
        nextX = x + dir[i][1]

        if nextX >= 0 and nextY >= 0 and nextX < m and nextY < n and visited[nextY][nextX] == False:
            visited[nextY][nextX] = True
            sum = max(sum, page[y][x] + DFS(nextY, nextX, cnt+1))
            visited[nextY][nextX] = False
    return sum

def middle(y, x):
    result = 0
    if y >= 1 and x >= 1 and x < m-1:
        result = max(result, page[y][x-1] + page[y][x] + page[y-1][x] + page[y][x+1])
    if y >= 1 and y < n-1 and x < m-1:
        result = max(result, page[y][x+1] + page[y][x] + page[y-1][x] + page[y+1][x])
    if y < n-1 and x >= 1 and x < m-1:
        result = max(result, page[y][x-1] + page[y][x] + page[y][x+1] + page[y+1][x])
    if y >= 1 and y < n-1 and x <= m-1:
        result = max(result, page[y][x-1] + page[y][x] + page[y-1][x] + page[y+1][x])
    return result

result = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        result = max(result, DFS(i,j,1))
        result = max(result, middle(i,j))
        visited[i][j] = False

print(result)