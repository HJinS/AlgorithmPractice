n = int(input())

stair = [0 for i in range(301)]
dp = [[0 for col in range(301)]for row in range(2)]

for i in range(1, n+1):
    stair[i] = int(input())

# 0 - 1칸 1 - 두칸
# 복습 필요
# 1차원 배열 가능

dp[0][1] = stair[1]
dp[1][1] = 0

dp[0][2] = dp[0][1] + stair[2]
dp[1][2] = stair[2]


for i in range(3,n+1):
    dp[0][i] = dp[1][i-1] + stair[i]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + stair[i]

print(max(dp[0][n], dp[1][n]))