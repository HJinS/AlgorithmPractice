#한번 더 풀기
n = int(input())
T = [0 for i in range(16)]
P = [0 for i in range(16)]
dp = [0 for i in range(16)]
for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())
    dp[i] = P[i]


for i in range(2,n+1):
    for j in range(1,i):
        if j + T[j] <= i:
            dp[i] = max(dp[i], dp[j] + P[i])
maxP = 0
for i in range(1,n+1):
    if T[i] + i <= n+1:
        maxP = max(dp[i], maxP)

print(maxP)