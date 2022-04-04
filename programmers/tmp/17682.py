from collections import deque
def solution(dartResult):
    idx = 0
    length = len(dartResult)
    dart = deque()
    while idx < length:
        end = idx+2
        while end < length and not dartResult[end].isdigit():
            end += 1
        dart.append(dartResult[idx: end])
        idx = end
    
    dart = list(dart)
    score_q = deque()
    total_score = 0
    for res in dart:
        if res[-1] == '*' or res[-1] == '#':
            score, bonus, option = res[:-2], res[-2], res[-1]
        else:
            score, bonus, option = res[:-1], res[-1], 'none'
        score = int(score)
        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        elif bonus == 'T':
            bonus = 3
        score = score ** bonus
        if option == '*':
            if score_q:
                last_score = score_q.pop()
                total_score += last_score
                last_score *= 2
                score_q.append(last_score)
            score_q.append(score*2)
            total_score += score*2
        elif option == '#':
            total_score -= score
            score_q.append(-score)
        elif option == 'none':
            total_score += score
            score_q.append(score)

        
    return total_score