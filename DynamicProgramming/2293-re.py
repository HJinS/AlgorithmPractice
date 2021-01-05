n, k = map(int, input().split())
dp = [0 for i in range(10001)]
coins = []

for i in range(n):
    coins.append(int(input()))

dp[0] = 1

for i in range(n):
    for j in range(min(coins),k+1):
        dp[j] += dp[j-coins[i]]

print(dp[k])