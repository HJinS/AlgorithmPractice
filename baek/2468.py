from collections import deque
height = []
N = int(input())
MIN, MAX = 100, 0
for i in range(N):
    height.append(list(map(int, input().split(' '))))
    rowMin = min(height[i])
    rowMax = max(height[i])
    MIN = min(MIN, rowMin)
    MAX = max(MAX, rowMax)
    
dir_x = [0, 1, 0, -1]
dir_y = [1, 0 ,-1, 0]
res = 0

def check_water(height_of_water: int):
    
    state = [[False for i in range(N)] for j in range(N)]
    
    for i in range(N):
        for j in range(N):
            if height[i][j] < height_of_water:
                state[i][j] = True
    
    def get_count(x, y):
        Q = deque()
        Q.append([x, y])
        
        while Q:
            currentX, currentY = Q.popleft()
            
            for i in range(4):
                n_x, n_y = currentX+dir_x[i], currentY+dir_y[i]
                if 0 <= n_x < N and 0 <= n_y < N:
                    if state[n_y][n_x] == False:
                        Q.append([n_x, n_y])
                        state[n_y][n_x] = True
    cnt = 0
    for i in range(N):
        for j in range(N):
            if state[i][j] == False:
                cnt += 1
                get_count(j, i)
    
    return cnt

for i in range(MIN, MAX+1):
    cnt = check_water(i)
    res = max(res, cnt)
    
print(res)
    