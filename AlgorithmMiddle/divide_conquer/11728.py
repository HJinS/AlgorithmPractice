from collections import deque
N, M = map(int, input().split())

A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
res = deque()

while N > 0 and M > 0:
    if A[0] > B[0]:
        num = B.popleft()
        M -= 1
        res.append(num)
    else:
        num = A.popleft()
        N -= 1
        res.append(num)
while N > 0:
    num = A.popleft()
    N -= 1
    res.append(num)

while M > 0:
    num = B.popleft()
    M -= 1
    res.append(num)
for e in res:
    print(e, end=' ')
