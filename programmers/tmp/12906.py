from collections import deque
def solution(arr):
    
    idx = 1
    num = arr[0]
    length = len(arr)
    ans = deque()
    ans.append(arr[0])
    
    for i in range(length):
        if arr[i] != ans[-1]:
            ans.append(arr[i])
    return list(ans)