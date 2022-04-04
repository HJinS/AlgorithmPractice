def solution(strings, n):
    arr = []
    for i in range(len(strings)):
        arr.append([strings[i][n], strings[i]])
    
    arr.sort()
    ans = []
    for item in arr:
        ans.append(item[1])
    return ans