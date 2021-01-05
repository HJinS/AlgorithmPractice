n = int(input())
dp = [[0 for i in range(501)] for j in range(501)]
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

dp[1][1] = tri[1][1]
for i in range(1,n+1):
    for j in range(1,i+1):
        if j != 1 and j != i:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i-1][j-1]
        elif j == 1:
            dp[i][j] = dp[i-1][j] + tri[i-1][j-1]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i-1][j-1]
        elif j == 1 and i == 1:
            continue
print(max(dp[n]))