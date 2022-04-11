from collections import deque
def solution(s):
    Q = deque()
    length = len(s)
    idx = 0
    
    s_list = list(s.split("},{"))
    
    for item in s_list:
        if item[:2] == "{{" and item[-2:] == "}}":
            item_sub = item[2:-2]
        elif item[:2] == "{{":
            item_sub = item[2:]
        elif item[-2:] == "}}":
            item_sub = item[:-2]
        else:
            item_sub = item[:]
        splited_list = list(map(int, item_sub.split(',')))
        Q.append(splited_list)
    
    Q = list(Q)
    
    sorted_by_length = sorted(Q, key=lambda x:len(x))
    ans = []
    for item in sorted_by_length:
        for num in item:
            if num not in ans:
                ans.append(num)
                
    return ans
            
    
    