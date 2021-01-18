n = int(input())
s = []
visited = [False for i in range(n)]

startTeam = 0
linkTeam = 0
res = 987654321

for i in range(n):
    s.append(list(map(int, input().split())))

def solve(start,cnt):
    global startTeam
    global linkTeam
    global res
    if cnt == n//2:
        startTeam = 0
        linkTeam = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == True and visited[j] == True:
                    startTeam += s[i][j]
                elif visited[i] == False and visited[j] == False:
                    linkTeam += s[i][j]
        res = min(res, abs(startTeam - linkTeam))
        return
                    
    for i in range(start, n):
        if visited[i] == False:
            visited[i] = True
            solve(i, cnt + 1)
            visited[i] = False
for i in range(n):
    solve(i,0)
print(res)