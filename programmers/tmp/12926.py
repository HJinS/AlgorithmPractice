def solution(s, n):
    
    res = ""
    for c in s:
        if c == ' ':
            res += c
            continue
        if ord('A') <= ord(c) <= ord('Z'):
            new_num = ord(c) + n
            if new_num > ord('Z'):
                new_num = ord('A') + (new_num-ord('Z')) - 1
        elif ord('a') <= ord(c) <= ord('z'):
            new_num = ord(c) + n
            if new_num > ord('z'):
                new_num = ord('a') + (new_num-ord('z')) - 1
        else:
            new_num = ord(c)
        res += chr(new_num)
    return res