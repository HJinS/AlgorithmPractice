def solution(s):
    flag = False
    word = ""
    for i in range(len(s)):
        if s[i] == ' ':
            flag = False
            word += ' '
            continue
        if not flag:
            word += s[i].upper()
        else:
            word += s[i].lower()
        flag = not flag
    return word