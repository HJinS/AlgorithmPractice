import sys
from heapq import heappop, heappush

inf = sys.maxsize
N = int(input())
edge = [[] for i in range(N+1)]

def dijkstra(start):
    dis = [inf for i in range(N+1)]
    heap = []
    heappush(heap, [start, 0])
    dis[start] = 0

    while heap:
        v, w = heappop(heap)
        for adj_v, adj_w in edge[v]:
            new_w = w + adj_w
            if dis[adj_v] > new_w:
                dis[adj_v] = new_w
                heappush(heap, [adj_v, new_w])
    return dis


for i in range(N):
    data = list(map(int, input().split()))
    for i in range(1, len(data), 2):
        if data[i] != -1:
            edge[data[0]].append([data[i], data[i+1]])

d = dijkstra(1)
print(max(dijkstra(d.index(max(d[1:])))[1:]))
