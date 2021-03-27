import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
arr = list(map(int, input().split()))
res_cnt = 0

def solve(start, end):
    global res_cnt, arr
    size = end - start
    mid = (start + end) // 2
    if size <= 1:
        return
    solve(start, mid)
    solve(mid, end)

    idx1, idx2 = start, mid
    new_arr = []
    cnt = 0
    while idx1 < mid and idx2 < end:
        if arr[idx1] > arr[idx2]:
            new_arr.append(arr[idx2])
            idx2 += 1
            cnt += 1
        else:
            new_arr.append(arr[idx1])
            idx1 += 1
            res_cnt += cnt
    while idx1 < mid:
        new_arr.append(arr[idx1])
        idx1 += 1
        res_cnt += cnt
    while idx2 < end:
        new_arr.append(arr[idx2])
        idx2 += 1

    for i in range(len(new_arr)):
        arr[start + i] = new_arr[i]

solve(0, N)
print(res_cnt)
