from collections import deque
def solution(str1, str2):
    A_set = deque()
    B_set = []
    str1 = str1.lower()
    str2 = str2.lower()
    for idx in range(0, len(str1)-1):
        if not str1[idx].isalpha() or not str1[idx+1].isalpha():
            continue
        A_set.append(str1[idx:idx+2])
        
    for idx in range(0, len(str2)-1):
        if not str2[idx].isalpha() or not str2[idx+1].isalpha():
            continue
        B_set.append(str2[idx:idx+2])
        
    str1_copy = A_set.copy()
    union = A_set.copy()
    intersection = deque()
    # 중복 된 것을 모으면 교집합, 기존 A에다가 중복을 제외한 것을 추가하면 합집합
    for c in B_set:
        if c in str1_copy:
            str1_copy.remove(c)
            intersection.append(c)
        else:
            union.append(c)
            
    if len(intersection) == 0 and len(union) == 0:
        return 65536
    else:
        res = int(len(intersection) / len(union) *65536)
        return res
    