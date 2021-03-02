N = int(input())

bulb = list(map(int, input()))
des = list(map(int, input()))

def first_on(state):
    cnt = 1
    state[0] = 1 - state[0]
    state[1] = 1 - state[1]
    for i in range(1, N):
        if state[i-1] != des[i-1]:
            state[i-1] = 1 - state[i-1]
            state[i] = 1 - state[i]
            if i != N-1:
                state[i+1] = 1 - state[i+1]
            cnt += 1
    
    if state != des:
        return -1
    else:
        return cnt

def first_off(state):
    cnt = 0
    for i in range(1, N):
        if state[i-1] != des[i-1]:
            state[i-1] = 1 - state[i-1]
            state[i] = 1 - state[i]
            if i != N-1:
                state[i+1] = 1 - state[i+1]
            cnt += 1

    if state != des:
        return -1
    else:
        return cnt

res1 = first_on(bulb[:])
res2 = first_off(bulb[:])

if res1 == -1 and res2 == -1:
    print(-1)
elif res1 == -1 and res2 != -1:
    print(res2)
elif res1 != -1 and res2 == -1:
    print(res1)
else:
    print(min(res1, res2))
