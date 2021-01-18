N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for i in range(N)]
res = 0

def solve(cnt ,sum):
    global res
    if cnt >= N:
        return
    sum += arr[cnt]
    if sum == S:
        res += 1
    solve(cnt + 1, sum - arr[cnt])
    solve(cnt + 1, sum)

solve(0, 0)
print(res)
