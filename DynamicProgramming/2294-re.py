n, k = map(int, input().split())
coins = []
dp = [1000000 for i in range(100001)]

for i in range(n):
    coins.append(int(input()))

dp[0] = 0
for i in range(n):
    for j in range(min(coins),k+1):
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)

if dp[k] == 1000000:
    print(-1)
else:
    print(dp[k])
