n = int(input())
dp = [0 for i in range(16)]
P = [0 for i in range(16)]
T = [0 for i in range(16)]

for i in range(1,n+1):
    T[i], P[i] = map(int, input().split())
    dp[i] = P[i]

for i in range(2, n+1):
    for j in range(1,i+1):
        if T[j] + j <= i:
            dp[i] = max(dp[i], dp[j] + P[i])

tmp = 0
for i in range(1, n+1):
    if i + T[i] <= n+1:
        tmp = max(tmp, dp[i])
print(tmp)