n = int(input())
tri = [0 for col in range(500)]
dp = [[0 for col in range(500)]for row in range(500)]

for i in range(n):
    tri[i] = list(map(int, input().split()))

dp[0][0] = tri[0][0]

#복습 필요

for i in range(1,n):
    for j in range(0,i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        elif j > 0 and j < i:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]


maxNum = dp[n-1][0]
for i in range(1,n):
    if maxNum < dp[n-1][i]:
        maxNum = dp[n-1][i]


print(maxNum)