def solution(n, arr1, arr2):
    
    res = []
    for i in range(n):
        res.append(arr1[i] | arr2[i])
    
    ans = []
    for r in res:
        map = r
        decoded = ""
        for i in range(n):
            remain = map % 2
            if remain == 1:
                decoded = "#"+decoded
            else:
                decoded = " "+decoded
            map //= 2
        ans.append(decoded)
    return ans