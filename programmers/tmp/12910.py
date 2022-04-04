from collections import deque
def solution(arr, divisor):
    ans = deque()
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            ans.append(arr[i])
    
    if not ans:
        ans.append(-1)
    ans = list(ans)
    ans.sort()
    return ans