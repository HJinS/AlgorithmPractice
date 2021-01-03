n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(1001)]
arr.insert(0,0)

dp[1] = arr[1]

res = 0

for i in range(1, n+1):
    sumNum = 0
    dp[i] = arr[i]
    for j in range(1,i):
        if arr[i] > arr[j]:
            sumNum = max(sumNum,dp[j] + arr[i])
    dp[i] = max(dp[i], sumNum)
    res = max(res,dp[i])

print(res)