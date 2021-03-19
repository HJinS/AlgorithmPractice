import sys
sys.setrecursionlimit(100000)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0]*(n+1)
for i in range(n):
    pos[in_order[i]] = i

def divide(in_start, in_end, p_start, p_end):
    if (in_start > in_end) or (p_start > p_end):
        return
    parent = post_order[p_end]
    print(parent, end=' ')

    left = pos[parent] - in_start
    right = in_end - pos[parent]

    divide(in_start, in_start+left-1, p_start, p_start+left-1)
    divide(in_end-right+1, in_end, p_end-right, p_end-1)

divide(0, n-1, 0, n-1)