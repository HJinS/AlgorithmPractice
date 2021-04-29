H, W = map(int, input().split())
N = int(input())

stickers = []
for i in range(N):
    stickers.append(list(map(int, input().split())))

def check(s1, s2):
    if s1[0] + s2[0] <= W and max(s1[1], s2[1]) <= H:
        return True
    if s1[1] + s2[1] <= H and max(s1[0], s2[0]) <= W:
        return True
    return False

ans = 0 
for i in range(N-1):
    for j in range(i+1, N):
        s1 = stickers[i]
        s2 = stickers[j]
        area = s1[0] * s1[1] +  s2[0] * s2[1]
        for k in range(1 << 2):
            s1 = stickers[i]
            s2 = stickers[j]
            if 1 << 1 & k:
                s1 = list(reversed(stickers[i]))
            if 1 << 0 & k:
                s2 = list(reversed(stickers[j]))
            if check(s1, s2):
                ans = max(ans, area)
print(ans)