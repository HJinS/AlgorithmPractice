N = int(input())

weightList = []
heightList = []

for i in range(N):
    weight, height = map(int, input().split(' '))
    weightList.append(weight)
    heightList.append(height)

rank = []

for i in range(N):
    cnt = 0
    for j in range(N):
        if j == i:
            continue
        else:
           if weightList[i] < weightList[j] and heightList[i] < heightList[j]:
               cnt += 1
    rank.append(cnt+1)
    
for i in range(N):
    print(rank[i], end=' ')
print()