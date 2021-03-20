import sys
sys.setrecursionlimit(100000)
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0]*(n+1)

for i in range(n):
    pos[in_order[i]] = i
 
def solve(in_start, in_end, pos_start, pos_end):
    if (in_start > in_end) and (pos_start > pos_end):
        return
    parent = post_order[pos_end]
    print(parent, end=' ')
    left = pos[parent] - in_start
    right = in_end - pos[parent]

    solve(in_start,in_start+left-1, pos_start, pos_start+left-1)
    solve(in_end-right+1, in_end, pos_end-right, pos_end-1)
solve(0, n-1, 0, n-1)