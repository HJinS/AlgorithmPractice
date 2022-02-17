from itertools import combinations
from collections import deque

N, M = map(int, input().split(' '))
MAP = []

for i in range(N):
    MAP.append(list(map(int, input().split(' '))))
    
chicken = deque()
house = deque()

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            house.append([j, i])
        elif MAP[i][j] == 2:
            chicken.append([j, i])
res = N * N * N
for item in combinations(chicken, M):
    chDis = 0
    for h in house:
        x, y = map(int, h)
        hMin = N * N
        for ch in item:
            cX, cY = map(int, ch)
            dis = abs(x - cX) + abs(y - cY)
            hMin = min(hMin, dis)
        chDis += hMin
    res = min(res, chDis)
print(res)
            
            