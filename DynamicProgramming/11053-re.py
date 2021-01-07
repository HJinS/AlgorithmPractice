n = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(1001)]
arr.insert(0,0)


for i in range(1,n+1):
    dp[i] = 1
    cnt = 0
    for j in range(1,i+1):
        if arr[i] > arr[j]:
            cnt = max(cnt, dp[j])
    dp[i] += cnt
print(max(dp))