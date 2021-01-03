n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(1001)]

arr.insert(0,0)

for i in range(n,0,-1):
    cnt = 0
    dp[i] = 1
    for j in range(n,i-1,-1):
        if arr[i] > arr[j]:
            cnt = max(cnt, dp[j])
    dp[i] += cnt

print(max(dp))