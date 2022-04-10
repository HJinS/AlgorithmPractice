from collections import deque
from itertools import permutations
def solution(expression):
    idx = 0
    length = len(expression)
    exp_Q = deque()
    exp_set = set()
    while idx < length:
        end = idx
        while end < length and expression[end].isdigit():
            end += 1
        
        if idx != end:
            exp_Q.append(int(expression[idx:end]))
            idx = end
        else:
            exp_set.add(expression[idx])
            exp_Q.append(expression[idx])
            idx += 1
            
    def calculation(pri):        
        Q = exp_Q.copy()
        for p in pri:
            mid_Q = deque()
            while Q:
                num = Q.popleft()
                if not Q:
                    mid_Q.append(num)
                    break
                else:
                    exp = Q.popleft()
                    
                
                if exp != p:
                    mid_Q.append(num)
                    mid_Q.append(exp)
                else:
                    num2 = Q.popleft()
                    if exp == "+":
                        res = num + num2
                    elif exp == "-":
                        res = num - num2
                    elif exp == "*":
                        res = num * num2
                    Q.appendleft(res)
            Q = mid_Q
            
        return Q[0]
    
    max_money = 0
    for p_item in permutations(list(exp_set)):
        p_item_list = list(p_item)
        res = calculation(p_item_list)
        max_money = max(max_money, abs(res))
    return max_money
        
                    
            
        
    
    