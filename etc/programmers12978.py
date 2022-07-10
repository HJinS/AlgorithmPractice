import sys

# Floyd-Warshall 알고리즘을 이용하면 쉽게 풀 수 있는 문제
# 사용시 mid(중간에 들르는 지점)에 대해 먼저 for문을 돌아야 한다 주의


def solution(N, road, K):
    dist = [[sys.maxsize for i in range(N)] for j in range(N)]

    for dis in road:
        s, e, d = dis
        dist[s - 1][e - 1] = min(dist[s - 1][e - 1], d)
        dist[e - 1][s - 1] = min(dist[e - 1][s - 1], d)

    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0

    for mid in range(N):
        for start in range(N):
            for end in range(N):
                if dist[start][end] > dist[start][mid] + dist[mid][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]
                    
    cnt = 0
    for dest in range(N):
        if dist[0][dest] <= K:
            cnt += 1

    return cnt