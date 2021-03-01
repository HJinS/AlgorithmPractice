from copy import deepcopy
N, M = map(int, input().split())
A = []
B = []
cnt = 0
result = True
for i in range(N):
    A.append(list(map(int, input())))
for i in range(N):
    B.append(list(map(int, input())))

def convert(x, y):
    for i in range(y, y+3):
        for j in range(x, x+3):
            A[i][j] = 1 - A[i][j]

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            convert(j, i)
            cnt += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            result = False
if not result:
    print("-1")
else:
    print(cnt)