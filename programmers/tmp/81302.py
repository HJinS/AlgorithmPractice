from collections import deque
from itertools import combinations
def solution(places):
    ans = []
    for room in places:
        s = deque()
        isOK = True
        for y in range(5):
            for x in range(5):
                if room[y][x] == "P":
                    s.append([x, y])
        
        for seats in combinations(s, 2):
            x1, y1 = seats[0][0], seats[0][1]
            x2, y2 = seats[1][0], seats[1][1]
            
            dis = abs(x2-x1) + abs(y2-y1)
            if dis <= 2:
                if x1 ==  x2:
                    if room[min(y1, y2)+1][x1] != "X":
                        isOK = False
                        print("line 22")
                        break
                elif y1 == y2:
                    if room[y1][min(x1, x2)+1] != "X":
                        isOK = False
                        break
                else:
                    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                        if room[y2][x1] != "X" or room[y1][x2] != "X":
                            isOK = False
                            break
                    elif (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
                        min_x, min_y = min(x1, x2), min(y1, y2)
                        max_x, max_y = max(x1, x2), max(y1, y2)
                        if room[min_y][min_x] != "X" or room[max_y][max_x] != "X":
                            isOK = False
                            print("line 40")
                            break
        if not isOK:
            ans.append(0)
        else:
            ans.append(1)
            
    return ans