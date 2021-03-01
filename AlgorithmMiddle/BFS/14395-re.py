from collections import deque
s, t = map(int, input().split())
visited = set()

def BFS():
    global s, t
    Q = deque()
    Q.append([s, ''])
    if s == t:
        return 0
    while Q:
        num, cal = Q.popleft()
        if num == t:
            return cal
        new_num = num * num
        if 0 <= new_num < 10e9 and new_num not in visited:
            visited.add(new_num)
            Q.append([new_num, cal+'*'])
        
        new_num = num + num
        if 0 <= new_num < 10e9 and new_num not in visited:
            visited.add(new_num)
            Q.append([new_num, cal+'+'])
        
        new_num = int(num // num)
        if 0 < new_num < 10e9 and new_num not in visited:
            visited.add(new_num)
            Q.append([new_num, cal+'/'])
    
    return -1

res = BFS()
print(res)