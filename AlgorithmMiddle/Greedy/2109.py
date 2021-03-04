import heapq

N = int(input())
lec = []

for i in range(N):
    lec.append(list(map(int, input().split())))

lec.sort(key=lambda x : x[1])
res = 0

sums = []
for lecture in lec:
    heapq.heappush(sums, lecture[0])
    if len(sums) > lecture[1]:
        heapq.heappop(sums)

print(sum(sums))