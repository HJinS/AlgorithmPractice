from heapq import heappop, heappush
import sys

inf = sys.maxsize
N = int(input())
edge = [[] for i in range(N+1)]

def dijkstra(start):
    heap = []
    dis = [inf for i in range(N+1)]
    dis[start] = 0
    heappush(heap, [start, 0])

    while heap:
        v, w = heappop(heap)
        
        for adj_v, adj_w in edge[v]:
            new_w = w + adj_w
            if dis[adj_v] > new_w:
                dis[adj_v] = new_w
                heappush(heap, [adj_v, new_w])
    return dis

for i in range(N-1):
    p, c, w = map(int, input().split())
    edge[p].append([c, w])
    edge[c].append([p, w])

d = dijkstra(1)
print(max(dijkstra(d.index(max(d[1:])))[1:]))