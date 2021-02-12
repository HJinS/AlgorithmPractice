N = int(input())
w = list(map(int, input().split()))

res = 0
def solve(sum, n):
    global res
    res = max(res, sum)
    if n <= 2:
        return
    for i in range(1, n-1):
        sum += w[i+1] * w[i-1]
        tmp = w.pop(i)
        solve(sum, n-1)
        w.insert(i, tmp)
        sum -= w[i+1] * w[i-1]
        


solve(0, N)
print(res)