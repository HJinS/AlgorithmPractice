n = int(input())
dp = [[0 for i in range(1000)] for j in range(3)]
RGB = []
for i in range(n):
    RGB.append(list(map(int, input().split())))
dp[0][0] = RGB[0][0]
dp[1][0] = RGB[0][1]
dp[2][0] = RGB[0][2]

res = 10000000005

for i in range(3):
    for j in range(3):
        if i == j:
            dp[j][0] = RGB[0][j]
        else:
            dp[j][0] = 10000000005
    for j in range(1, n):        
        dp[0][j] = min(dp[1][j-1], dp[2][j-1]) + RGB[j][0]
        dp[1][j] = min(dp[0][j-1], dp[2][j-1]) + RGB[j][1]
        dp[2][j] = min(dp[0][j-1], dp[1][j-1]) + RGB[j][2]
    for j in range(3):
        if i != j:
            res = min(res,dp[j][n-1])

print(res)