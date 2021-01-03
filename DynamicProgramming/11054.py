#복습 필요
#나눠서 양쪽에서 계산
n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(1001)]
lis = [0 for i in range(1001)]
lds = [0 for i in range(1001)]
arr.insert(0,0)

for i in range(1,n+1):
    lis[i] = 1
    cnt1 = 0
    for j in range(1,i):
        if arr[i] > arr[j]:
            cnt1 = max(cnt1, lis[j])
    lis[i] += cnt1

for i in range(n,0,-1):
    lds[i] = 1
    cnt2 = 0
    for j in range(n,i-1,-1):
        if arr[i] > arr[j]:
            cnt2 = max(cnt2, lds[j])
    lds[i] += cnt2

for i in range(n+1):
    dp[i] = lis[i] + lds[i] - 1

print(max(dp))