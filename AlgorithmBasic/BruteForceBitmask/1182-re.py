N, S = map(int, input().split())
arr = list(map(int ,input().split()))

visited = [False for i in range(N)]

res = 0

def solve(sum, cnt):
    global res
    if cnt >= N:
        return
    if sum + arr[cnt] == S:
        res += 1
    solve(sum+arr[cnt],cnt + 1)
    solve(sum, cnt + 1)

solve(0,0)
print(res)
