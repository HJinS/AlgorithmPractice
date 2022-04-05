def solution(s):
    list_s = list(s)
    list_s.sort(reverse=True)
    
    return "".join(list_s)