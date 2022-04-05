def solution(n):
    word1 = "수박"
    word2 = "수"
    res = ""
    for i in range(n//2):
        res += word1
    
    if n%2:
        res += word2
    return res