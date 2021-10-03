import sys
def solution(scores):
    
    mean_score = [0 for i in range(len(scores))]
    res = ["None" for i in range(len(scores))]
    stu_num = len(scores)
    
    for i in range(len(scores)):
        # i가 받은 점수
        sum_score = 0
        MIN, MAX = sys.maxsize, 0
        min_cnt, max_cnt = 0, 0
        for j in range(len(scores[0])):
            if scores[j][i] > MAX:
                MAX = scores[j][i]
                max_cnt = 1
            elif scores[j][i] == MAX:
                max_cnt += 1
            if scores[j][i] < MIN:
                MIN = scores[j][i]
                min_cnt = 1
            elif scores[j][i] == MIN:
                min_cnt += 1
            sum_score += scores[j][i]
        flag = False
        if scores[i][i] == MAX:
            if max_cnt == 1:
                sum_score -= scores[i][i]
                flag = True
        elif scores[i][i] == MIN:
            if min_cnt == 1:
                sum_score -= scores[i][i]
                flag = True
        if flag:
            mean_score[i] = sum_score / (stu_num-1)
        else:
            mean_score[i] = sum_score / stu_num
        
    for i in range(len(mean_score)):
        if mean_score[i] >= 90:
            res[i] = "A"
        elif 80 <= mean_score[i] < 90:
            res[i] = "B"
        elif 70 <= mean_score[i] < 80:
            res[i] = "C"
        elif 50 <= mean_score[i] < 70:
            res[i] = "D"
        else:
            res[i] = "F"
    return "".join(res)