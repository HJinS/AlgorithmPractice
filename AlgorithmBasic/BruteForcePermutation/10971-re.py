n = int(input())
w = []
visited = [False for i in range(n)]

res = 987654321

for i in range(n):
    w.append(list(map(int, input().split())))

def work(start, y, cnt, sum):
    global res
    if cnt == n and y == start:
        res = min(res, sum)
        return
    
    for i in range(n):
        if visited[y] == False and w[y][i] != 0:
            visited[y] = True
            sum += w[y][i]
            if sum <= res:
                work(start, i, cnt+1, sum)
            sum -= w[y][i]
            visited[y] = False
    return sum

for i in range(n):
    work(i,i,0,0)

print(res)

