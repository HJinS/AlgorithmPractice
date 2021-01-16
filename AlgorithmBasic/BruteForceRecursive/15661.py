N = int(input())
w = []
visited = [False for i in range(N)]
for i in range(N):
    w.append(list(map(int, input().split())))

startTeam = 0
linkTeam = 0
res = 987654321

def comb(start, cnt):
    global startTeam
    global linkTeam
    global res
    if cnt >=1 and cnt <= N-1:
        startTeam = 0
        linkTeam = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == True and visited[j] == True:
                    startTeam += w[i][j]
                elif visited[i] == False and visited[j] == False:
                    linkTeam += w[i][j]
        res = min(res, abs(startTeam - linkTeam))
    
    for i in range(start,N):
        if visited[i] == False:
            visited[i] = True
            comb(i, cnt + 1)
            visited[i] = False

comb(0, 0)

print(res)
