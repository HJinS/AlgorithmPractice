answer = 0
def solution(N, number):
    global answer
    cal(N, number, 0, 0)
    if answer > 8:
        answer = -1
    return answer
    
def cal(n, goal, cnt, sum):
    global answer
    if cnt > 8:
        return
    if sum == goal:
        if answer > cnt:
            answer = cnt
    tmp = 0
    for i in range(1, 8):
        tmp = (tmp*10) + n
        cal(n, goal, cnt+i, sum + tmp)
        cal(n, goal, cnt+i, sum - tmp)
        cal(n, goal, cnt+i, sum // tmp)
        cal(n, goal, cnt+i, sum * tmp)

solution(12, 5)