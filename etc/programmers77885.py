# 홀수 짝수 나누어서 경우 생각
# 작수 -> +1
# 혹수 -> 최하위 0 -> 1, 그 다음 1 -> 0
def solution(numbers):
    res = []
    for num in numbers:
        if num % 2 == 0:
            res.append(num + 1)
        else:
            tmp = num + 1
            complement_num = ~num + 1
            num = num | (complement_num & tmp)
            num = num & ~((complement_num & tmp) >> 1)
            res.append(num)
    return res