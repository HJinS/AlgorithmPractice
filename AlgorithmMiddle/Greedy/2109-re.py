from heapq import heappop, heappush
N = int(input())
lec = []
Q = []

for i in range(N):
    lec.append(list(map(int, input().split())))

lec.sort(key=lambda x : x[1])

for lecture in lec:
    heappush(Q, lecture[0])
    if len(Q) > lecture[1]:
        heappop(Q)
        
print(sum(Q))