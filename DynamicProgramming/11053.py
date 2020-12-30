n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(n)]

result = 0

# 복습 필요
# 2중 반복문

for i in range(n):
    dp[i] = 1
    cnt = 0
    for j in range(i+1):
        if arr[j] < arr[i]:
            cnt = max(cnt, dp[j])
    dp[i] += cnt
    result = max(result, dp[i])

print(result)

