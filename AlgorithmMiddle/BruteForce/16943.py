A, B = map(int, input().split())
arr = list(map(int, str(A)))

len_A = len(arr)
res = [0] * len_A
res_num = 0
visited = [False] * len_A

def solve(cnt):
    global res, res_num
    if cnt == len_A:
        tmp = 0
        for i in range(len_A):
            tmp += res[i] * 10 ** (len_A - i - 1)
        if tmp < B:
            res_num = max(res_num, tmp)
        return 

    for i in range(len_A):
        if not visited[i]:
            if cnt == 0 and arr[i] == 0:
                continue
            visited[i] = True
            res[cnt] = arr[i]
            solve(cnt+1)
            visited[i] = False

solve(0)
if res_num != 0:
    print(res_num)
else:
    print(-1)
