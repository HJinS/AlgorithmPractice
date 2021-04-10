N, M = map(int, input().split())

lesson = list(map(int, input().split()))

l, r = max(lesson), sum(lesson)
res = 10000

while l <= r:
    mid = (l + r) // 2
    lesson_sum = 0
    lesson_cnt = 0
    for i in range(N):
        lesson_sum += lesson[i]
        if lesson_sum > mid:
            lesson_sum = lesson[i]
            lesson_cnt += 1
    if lesson_sum != 0:
        lesson_cnt += 1

    if lesson_cnt > M:
        l = mid + 1
    elif lesson_cnt <= M:
        r = mid - 1

print(l)