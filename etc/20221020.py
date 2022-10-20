from collections import deque
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def get_num_str_from_q(Q):
    start_str = str(Q.popleft())
    end_str = None
    cnt = 0
    while Q:
        end_str = str(Q.popleft())
        cnt += 1
    if end_str:
        if cnt >= 2:
            result = start_str + '-' + end_str
        else:
            result = start_str + ',' + end_str
    else:
        result = start_str
    return result


def solution(args):
    Q = deque()
    answer = ''
    for item in args:
        if Q:
            last = Q[-1]
            diff = abs(item - last)
            if diff > 1:
                result = get_num_str_from_q(Q)
                answer = answer + result + ','
        Q.append(item)

    if Q:
        result = get_num_str_from_q(Q)
    answer = answer + result
    return answer
