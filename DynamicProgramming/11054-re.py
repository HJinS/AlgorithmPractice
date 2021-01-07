n = int(input())
arr = list(map(int, input().split()))
lis = [0 for i in range(1001)]
lds = [0 for i in range(1001)]
dp = [0 for i in range(1001)]

arr.insert(0,0)

for i in range(1,n+1):
    cnt = 0
    lis[i] = 1
    for j in range(1,i+1):
        if arr[i] > arr[j]:
            cnt = max(cnt, lis[j])
    lis[i] += cnt

for i in range(n,0,-1):
    cnt = 0
    lds[i] = 1
    for j in range(n,i-1,-1):
        if arr[i] > arr[j]:
            cnt = max(cnt, lds[j])
    lds[i] += cnt

for i in range(n+1):
    dp[i] = lis[i] + lds[i] - 1

print(max(dp))