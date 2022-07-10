import heapq
from collections import deque


def solution(a):
    H = deque()
    for idx, value in enumerate(a):
        H.append(-value)

    H = list(H)
    heapq.heapify(H)
    flag = False
    while len(H) > 1:
        max_n = heapq.heappop(H)
        second_n = heapq.heappop(H)
        max_n *= -1
        second_n *= -1
        cnt = 0
        while second_n == max_n:
            if not H:
                flag = True
                break
            third_n = heapq.heappop(H)
            heapq.heappush(H, -second_n)
            second_n = -third_n
            cnt += 1
            if cnt > len(H) - 1:
                flag = True
                break
        if flag:
            heapq.heappush(H, -max_n)
            heapq.heappush(H, -second_n)
            break
        diff = max_n - second_n
        heapq.heappush(H, -diff)
        heapq.heappush(H, -second_n)
    SUM = sum(H)
    SUM = -SUM
    return SUM

