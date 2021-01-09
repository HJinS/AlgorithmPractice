E, S, M = map(int, input().split())

e = m = s = 1
cnt = 1
while 1:
    if e == E and m == M and s == S:
        break

    e += 1
    m += 1
    s += 1
    cnt += 1
    if e > 15:
        e = 1
    if m > 19:
        m = 1
    if s > 28:
        s = 1
    
print(cnt)