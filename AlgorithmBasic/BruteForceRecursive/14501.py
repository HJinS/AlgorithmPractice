N = int(input())
T = [0 for i in range(16)]
P = [0 for i in range(16)]
dp = [0 for i in range(16)]
for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())
    dp[i] = P[i]

for i in range(1,N+1):
    for j in range(1, i+1):
        if i-j >= T[j]:
            dp[i] = max(dp[i], dp[j] + P[i])

maxNum = 0
for i in range(1,N+1):
    if T[i] + i <= N+1:
        maxNum = max(maxNum, dp[i])

print(maxNum)