import sys
#틀림
sys.setrecursionlimit(10**6)
res = 0
def solve(idx, total):
    global res
    if idx == len(op):
        res = max(res, int(total))
        return
    
    first = str(eval(total + op[idx] + nums[idx+1]))
    solve(idx + 1, first)

    if idx + 1 < len(op):
        second = str(eval(nums[idx+1] + op[idx+1] + nums[idx+2]))
        second = str(eval(total + op[idx] + second))
        solve(idx+2, second)

n = int(input())
formula = list(input())
nums, op = [], []
for e in formula:
    nums.append(e) if e.isdigit() else op.append(e)
solve(0, nums[0])
print(res)