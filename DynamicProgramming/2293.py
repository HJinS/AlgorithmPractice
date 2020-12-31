# 복습 필요
n, k = map(int, input().split())

coin = [0 for i in range(n)]
dp = [0 for i in range(k+1)]

for i in range(n):
    coin[i] = int(input())

dp[0] = 1


for i in range(n):
    for j in range(k+1):
        if j >= coin[i]:
            dp[j] += dp[j-coin[i]]

print(dp[k])