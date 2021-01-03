n, m = map(int, input().split())

room = []
for i in range(n):
    room.append(list(map(int, input().split())))

dp = [[0 for i in range(1000)] for j in range(1000)]

dp[0][0] = room[0][0]

for i in range(n):
    for j in range(m):
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j],dp[i][j-1])
        elif i-1 < 0:
            dp[i][j] = dp[i][j-1]
        elif j-1 < 0:
            dp[i][j] = dp[i-1][j]
        elif i==0 and j==0:
            continue
        dp[i][j] += room[i][j]
print(dp[n-1][m-1])