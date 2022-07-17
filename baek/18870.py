from collections import deque
N = int(input())

point = list(map(int, input().split(' ')))
res = [0 for i in range(N)]

info = deque()


items = [[idx, value] for idx, value in enumerate(point)]
sorted_items = sorted(items, key=lambda x:x[1])

for i in range(N):
    if info and sorted_items[i][1] == info[-1][1]:
        info[-1][0] += 1
        info[-1][2].append(sorted_items[i][0])
    else:
        info.append([1, sorted_items[i][1], [sorted_items[i][0]]])

print(info)
while info:
    count, value, idxs = info.pop()

    for idx in idxs:
        res[idx] = len(info)


for i in range(N):
    print(res[i], end=' ')
