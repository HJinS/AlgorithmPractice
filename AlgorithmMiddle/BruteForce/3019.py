C, P = map(int, input().split())

height = list(map(int, input().split()))
res = 0

if P == 1:
    res += C
    for i in range(C-3):
        if height[i] == height[i+1] == height[i+2] == height[i+3]:
            res += 1
elif P == 2:
    for i in range(C-1):
        if height[i] == height[i+1]:
            res += 1
elif P == 3:
    for i in range(C-2):
        if height[i] == height[i+1] and height[i+2] == height[i+1] + 1:
            res += 1
    for i in range(C-1):
        if height[i] == height[i+1] + 1:
            res += 1
elif P == 4:
    for i in range(C-2):
        if height[i+1] == height[i+2] and height[i] == height[i+1] + 1:
            res += 1
    for i in range(C-1):
        if height[i] + 1 == height[i+1]:
            res += 1
elif P == 5:
    for i in range(C-2):
        if height[i] == height[i+1] == height[i+2]:
            res += 1
    for i in range(C-1):
        if height[i] == height[i+1] + 1:
            res += 1
    for i in range(C-2):
        if height[i] == height[i+1] + 1 and height[i] == height[i+2]:
            res += 1
    for i in range(C-1):
        if height[i]+1 == height[i+1]:
            res += 1
elif P == 6:
    for i in range(C-2):
        if height[i] == height[i+1] == height[i+2]:
            res += 1
    for i in range(C-1):
        if height[i] == height[i+1]:
            res += 1

    for i in range(C-2):
        if height[i] + 1 == height[i+1] and height[i+1] == height[i+2]:
            res += 1
    for i in range(C-1):
        if height[i] == height[i+1]+2:
            res += 1
elif P == 7:
    for i in range(C-2):
        if height[i] == height[i+1] == height[i+2]:
            res += 1
    for i in range(C-1):
        if height[i] == height[i+1]:
            res += 1
    for i in range(C-2):
        if height[i+2] + 1 == height[i+1] and height[i] == height[i+1]:
            res += 1
    for i in range(C-1):
        if height[i]+2 == height[i+1]:
            res += 1
print(res)
