from collections import deque

S = input()
N = int(input())
Q = deque()
for i in range(N):
    Q.append(input())


idx = 0
length = len(S)

while idx < length:
    if S[:idx+1] in Q:
        S = S[idx+1:]
        length = len(S)
        idx = 0
    else:
        idx += 1

if len(S) != 0:
    print(0)
else:
    print(1)
