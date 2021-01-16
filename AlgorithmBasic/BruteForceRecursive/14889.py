N = int(input())
e = []
visited = [False for i in range(N)]
starteam = 0
linkteam = 0
for i in range(N):
    e.append(list(map(int, input().split())))

res = 987654321

def comb(start, cnt):
    global res
    if cnt == N//2:
        tmp = 0
        starteam = 0
        linkteam = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == True and visited[j] == True:
                    starteam += e[i][j]
                elif visited[i] == False and visited[j] == False:
                    linkteam += e[i][j]
        res = min(res,abs(starteam - linkteam))
        return
    
    for i in range(start,N):
        if visited[i] == False:
            visited[i] = True
            comb(i, cnt + 1)
            visited[i] = False

for i in range(N):
    comb(i,0)
print(res)