N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

visited = [False] * N
res = 0

def solve(cnt, idx, sum, min_num, max_num):
    global res
    if cnt >= 2:
        if L <= sum <= R and max_num - min_num >= X:
            res += 1
    
    for i in range(idx+1, N):
        if not visited[i]:
            visited[i] = True
            solve(cnt+1, i, sum+A[i], min(min_num, A[i]), max(max_num, A[i]))            
            visited[i] = False
            
solve(0, -1, 0, 10**7, 0)
print(res)