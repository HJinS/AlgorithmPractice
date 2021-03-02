from queue import PriorityQueue
from sys import stdin
N, K = map(int, stdin.readline().split())
Q = PriorityQueue()
jew = []
bag = []
sum = 0

for i in range(N):
    jew.append(list(map(int, stdin.readline().split())))

for i in range(K):
    bag.append(int(stdin.readline()))

jew.sort(key = lambda x : x[0])
bag.sort()

jew_ind = 0
for i in range(K):
    while jew_ind < N and bag[i] >= jew[jew_ind][0]:
        Q.put(jew[jew_ind][1]*(-1))
        jew_ind += 1
    if not Q.empty():
        sum += Q.get()

print(-sum)