from collections import deque
def solution(priorities, location):
    answer = 0
    list_Q = deque()
    
    for i in range(len(priorities)):
        list_Q.append([priorities[i], i])
        
    cnt = 0
    while True:
        e = list_Q.popleft()
        flag = True
        for i in range(len(list_Q)):
            if list_Q[i][0] > e[0]:
                list_Q.append(e)
                flag = False
                break
        if flag:
            cnt += 1
            if e[1] == location:
                answer = cnt
                break
    
    return answer