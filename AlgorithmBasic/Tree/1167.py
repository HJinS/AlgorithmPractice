from heapq import heappush, heappop
import sys

inf = sys.maxsize
N = int(input())
edge = [[] for i in range(N+1)]

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dis = [inf for i in range(N+1)]
    dis[start] = 0
    while heap:
        d, v = heappop(heap)
        for n_v, n_d in edge[v]:
            distance = d + n_d
            if dis[n_v] > distance:
                dis[n_v] = distance
                heappush(heap, [distance, n_v])
    return dis

for i in range(N):
    L = list(map(int ,input().split()))
    for j in range(1, len(L), 2):
        if L[j] != -1:
            edge[L[0]].append([L[j],L[j+1]])


di = dijkstra(1)
print(max(dijkstra(di.index(max(di[1:])))[1:]))