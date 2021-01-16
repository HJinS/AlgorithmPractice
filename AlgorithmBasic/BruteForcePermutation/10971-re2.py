N = int(input())
W = []
visited = [False for i in range(N)]
res = 987654321
for i in range(N):
    W.append(list(map(int, input().split())))

def work(start, y, cnt, sum):
    global res
    if cnt == N and start == y:
        res = min(res, sum)
        return
    
    for i in range(N):
        if W[y][i] != 0 and visited[y] == False:
            visited[y] = True
            sum += W[y][i]
            if sum <= res:
                work(start, i, cnt+1, sum)
            sum -= W[y][i]
            visited[y] = False
        
    return sum

for i in range(N):
    work(i,i,0,0)

print(res)