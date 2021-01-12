N, M = map(int, input().split())

visited = [[False for i in range(500)] for j in range(500)]
move = [[1,0], [-1,0], [0,1], [0,-1]]

box = []

for i in range(N):
    box.append(list(map(int, input().split())))

def DFS(y, x, cnt):
    
    if cnt == 4:
        return box[y][x]
    
    sum = 0
    for i in range(4):
        nextX = x + move[i][0]
        nextY = y + move[i][1]
        if nextX >= 0 and nextX < M and nextY >=0 and nextY < N and visited[nextY][nextX] == False:
            visited[y][x] = True
            sum = max(sum, box[y][x] + DFS(nextY, nextX, cnt+1))
            visited[y][x] = False
    return sum

def middle(y, x):
    result = 0
    if x >= 1 and y >= 1 and x < M-1:
        result = max(result, box[y][x] + box[y-1][x] + box[y][x-1] + box[y][x+1])
    if x >= 1 and y < N-1 and x < M-1:
        result = max(result, box[y][x] + box[y+1][x] + box[y][x-1] + box[y][x+1])
    if x < M-1 and y >= 1 and y < N-1:
        result = max(result, box[y][x] + box[y-1][x] + box[y+1][x] + box[y][x+1])
    if x >= 1 and y >= 1 and y < N-1:
        result = max(result, box[y][x] + box[y-1][x] + box[y+1][x] + box[y][x-1])
    return result

res = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        res = max(res, DFS(i, j, 1))
        res = max(res, middle(i, j))
        visited[i][j] = False

print(res)