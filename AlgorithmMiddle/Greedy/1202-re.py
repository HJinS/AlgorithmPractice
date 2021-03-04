from queue import PriorityQueue
from sys import stdin
N, K = map(int, stdin.readline().split())
jew = []
bag = []

for i in range(N):
    jew.append(list(map(int, stdin.readline().split())))

for i in range(K):
    bag.append(int(stdin.readline()))

jew.sort(key=lambda x : x[0])
bag.sort()
Q = PriorityQueue()
res = 0
jew_cnt = 0

for i in range(K):
    while jew_cnt < N and bag[i] >= jew[jew_cnt][0]:
        Q.put(jew[jew_cnt][1] * (-1))
        jew_cnt += 1
    if not Q.empty():
        res += Q.get()

print(res * (-1))