N, M, K = map(int, input().split())

team_G = int(N // 2)
left_G, left_M = 0, 0
if team_G > M:
    team = M
    left_G = N - 2 * M
    left_M = M - M
else:
    team = team_G
    left_M = M - team_G
    left_G = N - team_G * 2

if left_G > 0:
    K -= left_G
if left_M > 0:
    K -= left_M

if K <= 0:
    print(team)
else:
    if K % 3 == 0:
        team -= int(K // 3)
    else:
        team -= int(K // 3) + 1
    print(team)