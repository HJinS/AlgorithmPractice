n = int(input())

T = [0 for i in range(16)]
P = [0 for i in range(16)]
dp = [0 for i in range(16)]

## 추후 복습 필요

for i in range(1,n+1):
    T[i], P[i] = map(int, input().split())
    dp[i] = P[i]

for i in range(2, n+1):
    for j in range(1,i):
        if i-j >= T[j]:
            dp[i] = max(dp[j] + P[i], dp[i])

maxP = 0
for i in range(1,n+1):
    if i + T[i] <= n+1:
        maxP = max(maxP, dp[i])

print(maxP)
