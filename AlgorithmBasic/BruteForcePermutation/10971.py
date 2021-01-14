n = int(input())
w = []
visited = [False for i in range(10)]
global res
res = 987654321

for i in range(n):
    w.append(list(map(int, input().split())))

def solve(start, y, sum, cnt):
    global res
    if cnt == n and start == y:
        res = min(res, sum)
        return
    
    for i in range(n):
        if w[y][i] == 0:
            continue
        if visited[y] == False and w[y][i] > 0:
            visited[y] = True
            sum += w[y][i]

            if sum <= res:
                solve(start, i, sum, cnt + 1)
        
            visited[y] = False
            sum -= w[y][i]

for i in range(n):
    solve(i,i,0,0)

print(res)
